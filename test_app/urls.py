from django.contrib import admin
# include追加
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 追加
    path('', include('one_one.urls')),
]