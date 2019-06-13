# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import models


# Create your views here.


def index(request):
    pass
    return render(request, 'system/login.html')


@csrf_exempt
def login(request):

    """
    登录审查
    """

    if request.method == "POST":
        username = request.POST.get('username', None)  # 根据name属性获取
        password = request.POST.get('password', None)
        message = ""
        if username and password:
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/purchase/')  # 如果在这里传参 user
                else:
                    message = "密码错误，请重新输入。"
            except:
                message = "用户名错误，请重新输入"
        return render(request, 'system/login.html', {"message": message})
    return render(request, 'system/login.html')


def purchase(request):

    '''
    购入信息存入数据库
    :param request: 
    :return: 
    '''
    # 购入信息存入数据库
    if request.method == "POST":
        name = request.POST.get("name", None)
        number = request.POST.get("number", None)
        date = request.POST.get("date", None)
        type = request.POST.get("type", None)
        category = request.POST.get("category", None)
        part = request.POST.get("part", None)
        location = request.POST.get("location", None)

        tmp = models.Purchase(name=name, number=number, date=date
                                , type=type, category=category, part=part,
                                location=location)

        tmp.save()
        return redirect('/table/')
    return render(request, 'system/purchase.html')



def table(request):
    purchase_table = models.Purchase.objects.all()
    return render(request, 'system/table.html', {'purchase_table': purchase_table})

def dashboard(request):
    pass
    return render(request, 'system/dashboard.html')

def borrow(request):
    pass
    return render(request, 'system/borrow.html')

def broken(request):
    pass
    return render(request, 'system/broken.html')

def ruin(request):
    pass
    return render(request, 'system/ruin.html')

def search(request):
    pass
    return render(request, 'system/search.html')