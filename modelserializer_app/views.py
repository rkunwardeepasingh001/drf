from django.shortcuts import render
from .models import Account
from rest_framework import mixins,viewsets
from rest_framework import generics
from .serializer import CreateUserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

# class ModelserializerDetail(mixins.CreateModelMixin,
#                     mixins.ListModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     viewsets.GenericViewSet):
#     queryset = User.objects.all()
#     serializer_class = CreateUserSerializer


# from rest_framework.views import APIView
# class ModelserializerDetail(APIView):

#     def get(self, request ,pk=None):
#         if pk is not None:
#             user = User.objects.get(pk=pk)
#             serializer = CreateUserSerializer(user)
#             return Response(serializer.data)
#         else:
#             user = User.objects.all()
#             serializer = CreateUserSerializer(user,many=True)
#             return Response(serializer.data)
    

#     def post(self, request, format=None):
#         serializer = CreateUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


from rest_framework.views import APIView
from .serializer import AccountSerializer
# class AccountViews(APIView):

#     def get(self, request ,pk=None):
#         if pk is not None:
#             user = Account.objects.get(pk=pk)
#             serializer =AccountSerializer(user)
#             return Response(serializer.data)
#         else:
#             user = Account.objects.all()
#             serializer = AccountSerializer(user,many=True)
#             return Response(serializer.data)
    

#     def post(self, request, format=None):
#         serializer = AccountSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


class AccountViews(viewsets.ModelViewSet):
  serializer_class=AccountSerializer
  queryset=Account.objects.all()
#   serializer_class = AccountSerializer(queryset, context={'request': request})


 