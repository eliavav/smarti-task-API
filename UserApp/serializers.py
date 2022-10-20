from rest_framework import serializers
from UserApp.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('UserId', 'UserName', 'UserAddress', 'UserPhone')


