from .models import Account
from rest_framework import serializers
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']
        # depth = 1
        read_only_fields = ['account_name']

# class AccountSerializer(serializers.ModelSerializer):
#     url = serializers.CharField(source='get_absolute_url' )
#     groups = serializers.PrimaryKeyRelatedField(many=True)

#     class Meta:
#         model = Account
#         fields = ['url', 'groups']
        
from django.contrib.auth.models import User
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': { 'write_only': False }}

    def create(self, validated_data):
        #     email=validated_data['email'],
        #     username=validated_data['username']
        #     # password=validated_data['password']
        # )
        # user.set_password(validated_data['password'])
        # user.save()
        user=User.objects.create( email=validated_data['email'],
            username=validated_data['username'])
        return user


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    #     # model = Account
    #     # fields = ['url','id','account_name', 'users', 'created']
        model = Account
        fields = ['account_url','account_name', 'users', 'created']
        # extra_kwargs = {
        #     'url': {'view_name': 'accounts', 'lookup_field': 'account_name'},
        #     'users': {'lookup_field': 'username'}
        # }
        
        
        
        # url = serializers.HyperlinkedIdentityField(
        # view_name='accounts',
        #     lookup_field='slug'
        # )
        # users = serializers.HyperlinkedRelatedField(
        #     view_name='user-detail',
        #     lookup_field='username',
        #     many=True,
        #     read_only=True
        # )

        # class Meta:
        #     model = Account
        #     fields = ['url', 'account_name', 'users', 'created']







# from rest_framework.generics import ListAPIView