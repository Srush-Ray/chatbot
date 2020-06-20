from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('add',views.add,name='add'),
    path('delete/<id>/',views.delete,name='delete'),
    path('load/<id>/',views.load,name='load'),
    path('load/<id>/update/<uid>/',views.update,name='update'),
    path('logout',views.logout,name='logout')
]
