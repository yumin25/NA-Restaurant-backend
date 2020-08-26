from knox.auth import TokenAuthentication
from knox.models import AuthToken

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from members.serializers import UserSerializer, CreateUserSerializer, LoginUserSerializer


class CreateUserAPI(GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["password"]) < 6:
            body = {"message": "short password"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        if len(request.data["nickname"]) < 4 :
            body = {"message": "short nickname. at least 4 characters are required."}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class LoginAPI(GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )