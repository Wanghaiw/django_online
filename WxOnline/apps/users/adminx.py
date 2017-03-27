#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-27 20:51:35
# @Author  : wangxian
import xadmin
from .models import EmailVerifyRecord,UserProfile,Banner

class EmailVerifyRecordAdmin(object):
	list_display = ['code','email','send_type','send_time']
	search_fields = ['code','email','send_type','send_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)

class UserProfileAdmin(object):
	pass

xadmin.site.register(UserProfile,UserProfileAdmin)

class BannerAdmin(object):
	pass
xadmin.site.register(Banner,BannerAdmin)
