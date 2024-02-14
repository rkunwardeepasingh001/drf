from django.urls import path
from serializer_app.views import CommentAPIView,Field_validated
from serializer_app.serializer import CommentSerializer

urlpatterns=[
  path("CommentAPIView/",CommentAPIView.as_view()),
  path("CommentAPIView/<int:pk>/",CommentAPIView.as_view()),
  path("Field_validated/",Field_validated.as_view()),
  path("Field_validated/<int:pk>/",Field_validated.as_view()),
]