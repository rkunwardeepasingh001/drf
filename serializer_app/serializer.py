# from rest_framework import serializers
# from django.contrib.auth.models import User
# class Demoserializer(serializers.ModelSerializer):
#   class Meta:
#     model=User
#     fields=['username','password']





from rest_framework import serializers
from serializer_app.models import Comment 

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()



# serializer = CommentSerializer(Comment)
# a=serializer.data
# print(a)

from  rest_framework import serializers
from serializer_app.serializer import Comment 

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
#########################field-validation################################

class BlogPostSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def validate_content(self, value):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    

#########################-dealing with nested objects-###################
    
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class EditItemSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)

class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)
    edits = EditItemSerializer(required=False,many=True)
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


    