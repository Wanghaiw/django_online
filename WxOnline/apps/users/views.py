# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.backends import ModelBackend
# Create your views here.
from .models import UserProfile
from django.db.models import Q
from django.views.generic import View
from .forms import LoginForm



class CustomBackend(ModelBackend):
	'''重写django默认的登录方法authenticate 能通过邮箱验证  还需要在seeings里面配置AUTHENTICATION_BACKENDS'''
	def authenticate(self,username=None,password=None,**kwargs):
		try:
			user = UserProfile.objects.get(Q(username=username)|Q(email=username))
			if user.check_password(password):
				return user
		except Exception as e:
			return None
class LoginView(View):
	def get(self,request):
		return render(request, 'login.html', locals())
	def post(self,request):
		login_form = LoginForm(request.POST) #实例form表单
		if login_form.is_valid(): #判断表单是否符合要求
			user_name = request.POST.get('username', '')
			pass_word = request.POST.get('password', '')
			user = authenticate(username=user_name, password=pass_word)
			if user is not None:
				auth_login(request, user)
				return render(request, 'index.html')
			else:
				return render(request, 'login.html', {'msg': u'用户名或密码错误'})
		else:
			return render(request, 'login.html', {'login_form':login_form})


