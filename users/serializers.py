
from rest_framework import serializers

from users.models import User


class UserCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)

