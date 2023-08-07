from rest_framework import generics

from users.models import User
from users.serializers import UserSerializers, UserCreateSerializers



class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializers

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user_email = request.data['email']
    #     password = request.data['password']
    #     user = User.objects.create_user(email=user_email, password=password)
    #     get_new_user(user)
    #     user.save()


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

