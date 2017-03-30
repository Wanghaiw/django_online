#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-27 20:51:35
# @Author  : wangxian
import xadmin
from xadmin import views
from .models import EmailVerifyRecord,UserProfile,Banner

class BaseSetting(object):
	enable_themes = True
	use_bootswatch = True

class GlobalSettings(object):
	site_title = 'python后台管理系统'
	site_footer = '潭州教育'
	menu_style = 'accordion'

class EmailVerifyRecordAdmin(object):
	list_display = ['code','email','send_type','send_time'] #显示
	search_fields = ['code','email','send_type','send_time'] # 搜索
	list_filter = ['code','email','send_type','send_time'] #过滤

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)

class UserProfileAdmin(object):
	pass

xadmin.site.register(UserProfile,UserProfileAdmin)

class BannerAdmin(object):
	list_display = ['title','image','url','index','add_time'] #显示
	search_fields = ['title','image','url','index'] # 搜索
	list_filter = ['title','image','url','index','add_time']#过滤

xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)

xadmin.site.register(views.CommAdminView,GlobalSettings)