from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token 
from .views import *

urlpatterns = [
    
    path('', views.home, name='home'),
    path('delete/<one_id>', views.delete, name="delete"),
    path('edit/<one_id>', views.edit, name="edit"),
    path('test', views.test, name='test'),
    
    path('users/', UserList.as_view()),
    path('create-users/', UserCreate.as_view()),
    path('users/<pk>/', UserRetrieveUpdate.as_view()),
    path('ones/', OneListCreate.as_view()),
    path('ones/<pk>/', oneRetrieveUpdate.as_view()),
]