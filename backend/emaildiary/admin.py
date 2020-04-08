#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

from emaildiary.models import Diary, User


# 自定义添加界面
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        # 主键和必不可少的字段
        fields = ('email', 'name')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


# 自定义详情界面 / 编辑界面
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        # 用户类的字段
        fields = ('email', 'password', 'name', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial['password']


# 自定义 admin 可视化修改界面
class EmailDiaryUserAdmin(UserAdmin):
    form = UserChangeForm  # 详情界面 / 编辑界面
    add_form = UserCreationForm  # 添加界面

    # 显示的字段
    list_display = ('email', 'name', 'is_admin')
    # 过滤器字段
    list_filter = ('is_admin',)
    # 详情界面 / 编辑界面字段显示格式
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # 添加界面字段显示格式
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    # 搜索的字段范围
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, EmailDiaryUserAdmin)
admin.site.register(Diary)
admin.site.unregister(Group)
