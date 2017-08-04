# _*_ coding: utf-8 _*_
__author__ = 'Coder-Chandler'
__date__ = '2017.08.04 - 18:14'

import xadmin
from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
