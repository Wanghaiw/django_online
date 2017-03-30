#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-27 20:51:35
# @Author  : wangxian
import xadmin
from .models import *

class CityDictAdmin(object):
	list_display = ['name','desc','add_time'] #显示
	search_fields = ['name','desc'] # 搜索
	list_filter = ['name','desc','add_time'] #过滤

class CourseOrgAdmin(object):
	list_display = ['name','click_nums','fav_nums','address','city','add_time'] #显示
	search_fields = ['name','click_nums','fav_nums','address','city'] # 搜索
	list_filter = ['name','click_nums','fav_nums','address','city','add_time'] #过滤


class TeacherAdmin(object):
	list_display = ['name','work_years','work_company','work_position','click_nums','fav_nums','add_time'] #显示
	search_fields = ['name','work_years','work_company','work_position','click_nums','fav_nums'] # 搜索
	list_filter = ['name','work_years','work_company','work_position','click_nums','fav_nums','add_time'] #过滤



xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
