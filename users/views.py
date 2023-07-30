from rest_framework import generics

from users.models import User
from users.serializers import UserSerializers, UserCreateSerializers


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializers


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

