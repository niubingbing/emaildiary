#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    # 自定义用户管理员

    def create_user(self, email, name, password):
        if not email:
            raise ValueError('用户名不能为空！')
        if not password:
            raise ValueError('密码不能为空！')
        # normalize_email 将 @ 后面的邮件服务器名转为小写
        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_admin = True
        user.save()
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractBaseUser):
    # 自定义用户

    email = models.EmailField(verbose_name='Email address', max_length=320, unique=True)
    name = models.CharField(max_length=32)

    # 邮件提醒，默认开启每日提醒
    daily_remind = models.BooleanField(default=True)
    weekly_remind = models.BooleanField(default=False)
    monthly_remind = models.BooleanField(default=False)
    yearly_remind = models.BooleanField(default=False)

    # 统计数据，默认开启年报订阅
    weekly_report = models.BooleanField(default=False)
    monthly_report = models.BooleanField(default=False)
    yearly_report = models.BooleanField(default=True)

    # 删除用户时可以仅把 is_active 设置为 False，不真正删除用户
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # 用于 User.objects.all()
    objects = UserManager()

    USERNAME_FIELD = 'email'  # 主键 / 唯一标识
    REQUIRED_FIELDS = ['name']  # 不可少的字段

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        # TODO: staff == admin
        return self.is_admin


class Diary(models.Model):
    user: User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='diaries')
    title: str = models.TextField()
    content: str = models.TextField()
    release_time: datetime.datetime = models.DateTimeField(auto_now=True)
    update_time: datetime.datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 二元组 (用户, 发布时间) 作为日记的主键 / 唯一标识
        constraints = [models.UniqueConstraint(fields=['user', 'release_time'], name='diary_unique')]
        verbose_name_plural = 'diaries'

    def __str__(self):
        return f'user: {self.user} release_time: {self.release_time} title: {self.title}'
