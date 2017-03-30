#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-27 20:51:35
# @Author  : wangxian
import xadmin
from .models import *




class UserAskAdmin(object):
	list_display = ['name','mobile','course_name','add_time'] #显示
	search_fields = ['name','mobile','course_name'] # 搜索
	list_filter = ['name','mobile','course_name','add_time']#过滤

class CourseCommentsAdmin(object):
	list_display = ['user','course','comment','add_time'] #显示
	search_fields = ['user','course','comment'] # 搜索
	list_filter = ['user','course','comment','add_time']#过滤

class UserFavoriteAdmin(object):
	list_display = ['user','fav_id','fav_type','add_time'] #显示
	search_fields = ['user','fav_id','fav_type'] # 搜索
	list_filter = ['user','fav_id','fav_type','add_time']#过滤

class UserMessageAdmin(object):
	list_display = ['user','message','has_read','add_time'] #显示
	search_fields = ['user','message','has_read'] # 搜索
	list_filter = ['user','message','has_read','add_time']#过滤

class UserCourseAdmin(object):
	list_display = ['user','course','add_time'] #显示
	search_fields = ['user','course'] # 搜索
	list_filter = ['user','course','add_time']#过滤

xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
