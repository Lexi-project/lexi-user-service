from typing import Optional
from enum import Enum
from django.db import transaction
import grpc
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.tokens import BlacklistMixin
from django.core.exceptions import ValidationError
from credits.grpc.grpc_files import credit_pb2, credit_pb2_grpc
from credits.models import CreditTransaction
from userapp.models import Account, User

class TansactionStatus(Enum):
    SUCCESS = 'SUCCESS'
    PENDING = 'PENDING'
    FAILURE = 'FAILURE'


def get_user_from_token(token: str) -> Optional[User]:
    try:
        access_token = AccessToken(token)
        BlacklistMixin.check_blacklist(access_token)
        user_id = access_token.payload.get('user_id')
        user = User.objects.get(id=user_id)
        return user
    except Exception as e:
        return None


class CreditServiceServicer(credit_pb2_grpc.CreditServiceServicer):

    @transaction.atomic()
    def BorrowCredit(self, request, context):
        user = get_user_from_token(request.token)
        account = Account.objects.get(user=user)

        if request.credits <= 0 or account.credits < request.credits:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return credit_pb2.BorrowCreditResponse()
        
        new_transaction = CreditTransaction.objects.create(credits=request.credits)
        account.credits = account.credits - new_transaction.credits
        account.save()
        return credit_pb2.BorrowCreditResponse(transaction_id=new_transaction.id) 

    @transaction.atomic()
    def RollbackCredit(self, request, context):
        transaction = CreditTransaction.objects.get(id=request.transaction_id)
        user = get_user_from_token(request.token)
        account = Account.objects.get(user=user)
        account.credits = account.credits + transaction.credits
        account.save()
        transaction.status = TansactionStatus.FAILURE.value
        transaction.save()
        return credit_pb2.RollbackCreditResponse(is_success=True)
    
        
    def CommitCredit(self, request, context):
        transaction = CreditTransaction.objects.get(id=request.transaction_id)
        transaction.status = TansactionStatus.SUCCESS.value
        transaction.save()
        return credit_pb2.CommitCreditResponse(is_success=True)
