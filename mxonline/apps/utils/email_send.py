# _*_ coding: utf-8 _*_
__author__ = 'Coder-Chandler'
__date__ = '2017.08.06 - 18:21'
import string
from random import random
from mxonline.settings import EMAIL_FROM
from django.core.mail import send_mail
from users.models import EmailVerifyRecord


def random_str(randomlength):
    return ''.join(random.sample(string.ascii_letters + string.digits, randomlength))


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '慕学在线注册激活链接'
        email_body = '请点击下方链接激活你的账号:http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email_record])
        if send_status:
            pass
