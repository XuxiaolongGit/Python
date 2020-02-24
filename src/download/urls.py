"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path,include
#站点起始视图 ，由于没有多个功能，因此放弃使用，直接使用teacher中的视图
from . import views

app_name = 'download'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.books,name='books'),
    path('books_admin/',views.books_admin,name='books_admin'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('delete/',views.delete,name='delete'),
    path('upload/',views.upload,name='upload'),
    path('download/<int:pk>',views.download,name='download'),
    path('login',views.login,name='login'),
]
