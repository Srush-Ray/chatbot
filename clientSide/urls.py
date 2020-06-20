from django.urls import path,re_path
from django.conf.urls import url
from .views import chat,room

urlpatterns=[
    path('chat',chat,name='chat'),
    re_path(r'^(?P<room_name>[^/]+)/$', room,name='room'),

]
