# _*_ coding: utf-8 _*_
__author__ = 'Coder-Chandler'
__date__ = '2017.08.14 - 13:00'

from django.conf.urls import url, include
from .views import UserinfoView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name='user_info'),
]