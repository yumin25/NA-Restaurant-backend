from knox.auth import TokenAuthentication
from knox.models import AuthToken

from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .models import User

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
                "token": AuthToken.objects.create(user)[1],
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UpdateUserAPI(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self):
        return self.request.user

    def patch(self, request, user_region):
        instance = self.get_object()
        instance.user_region = user_region
        instance.save()
        print(instance)

        serializer = UserSerializer(instance)
        return Response(serializer.data)