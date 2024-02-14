from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser,FileUploadParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from django.contrib.auth.models import User

# # @csrf_exempt
# @api_view(['GET','POST','PUT'])  #these decorator is used for function based view !
# # def snippet_list(request):
# ##suffixes
# def snippet_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         l = JsonResponse(serializer.data, safe=False,status=206)
#         print(type(l))
#         # return JsonResponse(serializer.data, safe=False,status=206)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:  
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
    
# from rest_framework import status

# @api_view(['GET', 'PUT', 'DELETE','PATCH'])
# # def snippet_detail(request, pk):
# ##suffixes
# def snippet_detail(request, pk,format=None ):

#     """
#     Retrieve, update or delete a code snippet.
#     """
#     import pdb;pdb.set_trace()
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    


# from rest_framework import status
# from rest_framework.views import APIView
# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#    

# from django.http import Http404
# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# from rest_framework import status
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework import mixins
# from rest_framework import generics

# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request,self.queryset, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

  
    
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         id = kwargs.get("pk")
#         qs = self.queryset.get(id=id)
#         ser = self.serializer_class(qs, request.data,partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)





# from pygments.lexers import get_lexer_by_name
# from pygments.formatters.html import HtmlFormatter
# from pygments import highlight
# def save(self, *args, **kwargs):
#     """
#     Use the `pygments` library to create a highlighted HTML
#     representation of the code snippet.
#     """
#     lexer = get_lexer_by_name(self.language)
#     linenos = 'table' if self.linenos else False
#     options = {'title': self.title} if self.title else {}
#     formatter = HtmlFormatter(style=self.style, linenos=linenos,
#                               full=True, **options)
#     self.highlighted = highlight(self.code, lexer, formatter)
    # super().save(*args, **kwargs)



#####################################################################3
# class ListUsers(APIView):
#     """
#     View to list all users in the system.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAdminUser]

#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)

# @api_view()
# def hello(request):
# #   return Response({'msg':'deepak singh'})
#   return Response("deepak")

# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": 'request.data'})
#     return Response({"message": "Hello, world!"})


# from rest_framework.decorators import api_view, schema
# from rest_framework.schemas import AutoSchema

# class CustomAutoSchema(AutoSchema):
#     def get_link(self, path, method, base_url):
#         pass
# @api_view(['GET'])
# @schema(CustomAutoSchema())
# def view(request):
#     return Response({"message": "Hello for today! See you tomorrow!"})

# from django.contrib.auth.models import User
# from snippets.serializers import UserSerializer
# from rest_framework import generics
# from rest_framework.permissions import IsAdminUser


# class UserList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [IsAdminUser]
     
   
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = SnippetSerializer(queryset, many=True)
#         return Response(serializer.data)




####################################-VIEWSET-##########################################


from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from snippets.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class UserViewSet(viewsets.ViewSet):
    # import pdb;pdb.set_trace()
    queryset = User.objects.all()


    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

    def create(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("invalid data") 
    
    def update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        
        return Response("update-invalid-data")

        
    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)     
        return Response(" partial-update-invalid-data")
     
    def destroy(self, request, pk, format=None):
        item = get_object_or_404(self.queryset, pk=pk,)
        item.delete()
        return Response("-deleted-")
    

    
## IT EXECUTE WHEN SUPERUSER IS LOGIN:
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    

####################################-END-VIEWSET-####################################

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from snippets.serializers import UserSerializer,Password1Serializer
from rest_framework.permissions import IsAdminUser
# class Password1(viewsets.ReadOnlyModelViewSet):
class Password1(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post','get','put','patch','delete'],name="change password")

    # @action(methods=['post'], detail=True, permission_classes=[IsAdminUser])

 
    # @action(methods=['post'], detail=True, permission_classes=[IsAdminUser],
            # url_path='/<int:pk>/change-password', url_name='change_password')
    
    def set_password1(self, request, pk=None):
        user = self.get_object()
        serializer = Password1Serializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password']) 
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def recent_users(self, request):
        recent_users = User.objects.all().order_by('-last_login')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)
    
    @action(detail=True,methods=(['get','delete']))
    def delete_password(self, request, pk=None):
        user=self.get_object()

        user.password = ''
    
        user.save()
        return Response("deleted")
        # return Response("invalid")

from rest_framework import mixins

class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



####################################-END-VIEWSET-####################################
####################################-   PARSER -####################################
    
# @action(methods=['get','post','retrieve'])
class ExampleView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    # parser_classes = [JSONParser]
    user=User.objects.all()

    def post(self, request, format=None):
        return Response({"data-posted":request.data})
    

    def get(self,request,format=None): 
        serializer=UserSerializer(self.user, many=True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk,format=None):
        user = get_object_or_404(self.user,pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    


