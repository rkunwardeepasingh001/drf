from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter,SimpleRouter
# from .views import ModelserializerDetail,AccountserializerDetail
from .views import AccountViews,high_score
urlpatterns=[
  # path("ModelserializerDetail/",ModelserializerDetail.as_view()),
  # path("ModelserializerDetail/<int:pk>/",ModelserializerDetail.as_view()),
  # path("AccountViews/",AccountViews)
  path("high_score/",high_score)

]
router=DefaultRouter()
# router.register(r'ModelserializerDetail',ModelserializerDetail.as_view(),basename='create')
router.register(r'AccountViews',AccountViews)

urlpatterns += router.urls
