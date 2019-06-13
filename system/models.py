# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    '''用户表'''

    gender = (
        ('male', '男'),
        ('female', '女'),
    )

#    POS = (
#        ('U', '使用人员'),
#       ('A', '管理人员')
#   )

    name = models.CharField(max_length=128, unique=True, primary_key=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)
#   position = models.CharField(max_length=1, choices=POS)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Purchase(models.Model):
    '''
    被谁购入信息记录表
    '''

    date = models.CharField(max_length=128,  verbose_name="时间")
    name = models.CharField(max_length=128,  verbose_name="设备名称")
    type = models.CharField(max_length=128,  verbose_name="型号")
    category = models.CharField(max_length=128,  verbose_name="种类")
    number = models.BigIntegerField(unique=True, primary_key=True, verbose_name="编号 ")
    part = models.CharField(max_length=128, verbose_name="所属部门")
    location = models.CharField(max_length=128,  verbose_name="存放位置")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['number']
        verbose_name = '购入信息'
        verbose_name_plural = '购入信息'




