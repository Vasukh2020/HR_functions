"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from hello.views import *
from AceLogin.views import *
from django.contrib import admin
# from Article.views import *

urlpatterns = [

#the AceLogin part of url

path('register/', register, name='register'),
path('login/', login, name='login'),
path('info/', information, name='information'),

path('logout/',logout, name='logout'),
path('<int:pk>/ddvc/', dynamic_AceInformation, name='dynamic_AceInformation'),

#part of hello study
    path('', home_view, name='home'),
    path('l/', lhome_view, name='lview'),
    path('r/', view),
    path('side1/',side1),
    path('side2/',side2),
   path('ex/', extend_part),
   path('<int:pk>/detail/',product_detail_view),
   path('datad/' ,product_create_view,),
    path('getpost/' ,product_create_view,), path('dgetpost/' ,product_create_view,),

    path('admin/', admin.site.urls),
    path('product_view/', product_list_view,  name='list'), 
    path('creating/', creating),
    path('<int:pk_>/deleting/', deleting, name='delete'),
    path ('<int:id_>/update_venue/', update_venue, name='update-venue'),
    path('<int:pk>/ddv/', dynamic_detail_view, name='ddetailview'),
    path('<int:pk>/dupdate/', dynamic_update, name='dynamic-update'),
    path('<int:pk_>/ddelete/', dynamic_delete, name='dynamic-delete'),
    path('todelete/', product_list_view, name='delete-list')



     # path('', home, name='home'),
    #path('',ArticleListView.as_view(), name='article-list'),
    # path('<int:pk>/',ArticleDetailView.as_view(), name='article-detail'),
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
    ## path('<int:pk>/update',ArticleUpdateView.as_view(), name='article-update'),
    # path('<int:pk>/delete',ArticleDeleteView.as_view(), name='article-delete'),
    #path('<str:pk>/updatefx/', ArticleUpdate, name='function-create')

  

]

