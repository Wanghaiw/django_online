#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-27 20:51:35
# @Author  : wangxian
import xadmin
from .models import *

class CourseAdmin(object):
	list_display = ['name','degree','learn_times','students','fav_nums','click_nums','add_time'] #显示
	search_fields = ['name','degree','learn_times','students','fav_nums','click_nums'] # 搜索
	list_filter = ['name','degree','learn_times','students','fav_nums','click_nums','add_time'] #过滤


class LessonAdmin(object):
	list_display = ['course','name','add_time']
	search_fields = ['course','name']
	list_filter = ['course__name','name','add_time']

class CourseResourceAdmin(object):
	list_display = ['course','name','add_time','download']
	search_fields = ['course','name','download']
	list_filter = ['course','name','add_time','download']

class VideoAdmin(object):
	list_display = ['lesson','name','add_time']
	search_fields = ['course','name']
	list_filter = ['lesson','name','add_time']



xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
xadmin.site.register(Video,VideoAdmin)

