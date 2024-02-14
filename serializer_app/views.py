from django.shortcuts import render
from serializer_app.serializer import CommentSerializer,Comment
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework import serializers


# Create your views here.
class CommentAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request,*args, **kwargs):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment,many=True)
        return Response(serializer.data)


from .serializer import BlogPostSerializer
from django.shortcuts import get_object_or_404

class Field_validated(APIView):
    q=Comment.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        serializer = CommentSerializer(self.q, many=True)
        return Response(serializer.data)
 
    # def get(self, request, pk=None):
    #     user = get_object_or_404(self.q, pk)
    #     serializer = BlogPostSerializer(user)
    #     return Response(serializer.data)
  
#   def put(self, request):
#       user = get_object_or_404(self.queryset)
#       serializer=BlogPostSerializer(user,data=request.data)
#       if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)        
#       return Response("update-invalid-data")
  
        
    # def patch(self, request, pk=None):
    #     user = get_object_or_404(self.queryset, pk=pk)
    #     serializer=BlogPostSerializer(user,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)     
    #     return Response(" partial-update-invalid-data")
    
   
   
   