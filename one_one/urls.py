from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<one_id>', views.delete, name="delete"),
    path('edit/<one_id>', views.edit, name="edit"),
    path('test', views.test, name='test')
]