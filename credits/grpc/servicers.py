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

    def BorrowCredit(self, request, context):
        try:
            user = get_user_from_token(request.token)
            account = Account.objects.get(user=user)

            if request.credits <= 0:
                context.set_details('Invalid credits value')
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return credit_pb2.BorrowCreditResponse()
            
            if account.credits < request.credits:
                context.set_details('You do not have enough credits in your account')
                context.set_code(grpc.StatusCode.RESOURCE_EXHAUSTED)
                return credit_pb2.BorrowCreditResponse()
            
            transaction = CreditTransaction.objects.create(credits=request.credits)
            return credit_pb2.BorrowCreditResponse(transaction_id=transaction.id)
                
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            return credit_pb2.BorrowCreditResponse()

