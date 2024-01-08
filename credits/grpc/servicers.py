
from credits.grpc.grpc_files import credit_pb2, credit_pb2_grpc


class CreditServiceServicer(credit_pb2_grpc.CreditServiceServicer):

    def BorrowCredit(self, request, context):
        return credit_pb2.BorrowCreditResponse(transaction_id=1)
    
    def RollbackCredit(self, request, context):
        return credit_pb2.RollbackCreditResponse(is_success=True)
    
    def CommitCredit(self, request, context):
        return credit_pb2.CommitCreditResponse(is_success=True)
