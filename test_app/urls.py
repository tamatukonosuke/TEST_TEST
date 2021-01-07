from django.contrib import admin
# include追加
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token 
from django.conf.urls import include


urlpatterns = [
    path('auth/', obtain_jwt_token),
    path('admin/', admin.site.urls),
    path('api/', include('one_one.urls')),
    path('', include('one_one.urls')),
]