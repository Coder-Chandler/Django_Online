# _*_ coding: utf-8 _*_
__author__ = 'Coder-Chandler'
__date__ = '2017.08.08 - 19:43'

from django.conf.urls import url, include
from .views import OrgView, AddUserAskView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask')
]