from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        token = super().validate(attrs)

        return {'token': token.get('access'), 'user_id': self.user.id}
