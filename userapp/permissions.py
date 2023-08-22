from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsTokenValid(BasePermission):
    blacklist_model = BlacklistedToken
    outstanding_list_model = OutstandingToken

    def has_permission(self, request: Request, view):
        token = str(request.auth.token)[2:-1]
        try:
            outstanding_token = self.outstanding_list_model.objects.get(
                token=token)
            is_blacklisted = self.blacklist_model.objects.get(
                token_id=outstanding_token.id)
            return not is_blacklisted
        except (OutstandingToken.DoesNotExist, BlacklistedToken.DoesNotExist):
            return False
