from django.urls import path,include
from snippets.views import UserViewSet
from rest_framework.routers import SimpleRouter,DefaultRouter
from snippets.views import UserViewSet,Password1,CreateListRetrieveViewSet,ExampleView
# from snippets import views
# urlpatterns = [
#     path('snippets/', views.SnippetList),
#     path('snippets/<int:pk>/', views.SnippetDetail),
# ]

urlpatterns = [
    # path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    # path('hello/',views.hello),
    # path('hello WORLD/',views.hello_world),
    # path('aa/',views.UserList.as_view()),
    # path('aadd/',UserViewSet.as_view({'get':'list'})),
    # path('aafgf/<int:pk>/',UserViewSet.as_view({'get':'retrieve'})),
    path('ExampleView/',ExampleView.as_view()),
    path('ExampleView/<int:pk>/',ExampleView.as_view()),
    # path('roouter/',include('router.urls')),
     
  
]  

# from rest_framework.urlpatterns import format_suffix_patterns
# urlpatterns = format_suffix_patterns(urlpatterns,allowed=['json','html'])

####################################-VIEWSET-##########################################
# router = SimpleRouter(use_regex_path=False)
# router=SimpleRouter(trailing_slash=False)

# router=DefaultRouter()
router = SimpleRouter(trailing_slash=False)  
router.register(r"users",UserViewSet)
router.register(r"password1/",Password1)
router.register(r"mixin",CreateListRetrieveViewSet)

urlpatterns += router.urls

####################################-END-VIEWSET-######################################

# router.register(r"ExampleView",ExampleView.as_view())


