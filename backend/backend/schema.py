# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
import datetime
import json
import re

import graphene
import graphql_jwt
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from graphql_jwt.decorators import login_required, staff_member_required

from backend.error_messages import *
from emaildiary.models import Diary, User


class ErrorMessage:
    code: int
    message: str

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return json.dumps({
            'code': self.code,
            'message': self.message
        })


class UserType(DjangoObjectType):
    class Meta:
        model = User


class DiaryType(DjangoObjectType):
    class Meta:
        model = Diary


class CreateUser(graphene.Mutation):
    # 创建用户

    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        name = graphene.String()

    def mutate(self, info, email: str, password: str, **kwargs) -> 'CreateUser':
        if not re.search(r'[\w!#$%&\'*+/=?^_`{|}~-]+(?:\.[\w!#$%&\'*+/=?^_`{|}~-]+)*'
                         r'@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/', email):
            raise GraphQLError(str(ErrorMessage(
                code=invalid_email_code,
                message=invalid_email_message)))
        users = User.objects.filter(email=email)
        if users:
            user = users[0]
            if user.is_active:
                raise GraphQLError(str(ErrorMessage(
                    code=user_already_exist_code,
                    message=user_already_exist_message)))
            else:
                user.delete()
        user = get_user_model()(email=email, password=password)
        if 'name' in kwargs:
            user.name = kwargs['name']
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):
    # 更新用户

    user = graphene.Field(UserType)

    class Arguments:
        password = graphene.String()
        name = graphene.String()

    @login_required
    def mutate(self, info, **kwargs) -> 'UpdateUser':
        user = info.context.user
        updated = False
        if 'password' in kwargs:
            user.set_password(kwargs['password'])
            updated = True
        if 'name' in kwargs:
            user.name = kwargs['name']
            updated = True
        if 'daily_remind' in kwargs:
            user.daily_remind = kwargs['daily_remind']
            updated = True
        if 'weekly_remind' in kwargs:
            user.weekly_remind = kwargs['weekly_remind']
            updated = True
        if 'monthly_remind' in kwargs:
            user.monthly_remind = kwargs['monthly_remind']
            updated = True
        if 'yearly_remind' in kwargs:
            user.yearly_remind = kwargs['yearly_remind']
            updated = True
        if 'weekly_report' in kwargs:
            user.weekly_report = kwargs['weekly_report']
            updated = True
        if 'monthly_report' in kwargs:
            user.monthly_report = kwargs['monthly_report']
            updated = True
        if 'yearly_report' in kwargs:
            user.yearly_report = kwargs['yearly_report']
            updated = True
        if not updated:
            raise GraphQLError(str(ErrorMessage(
                code=update_user_no_parameters_code,
                message=update_user_no_parameters_message)))
        user.save()

        return UpdateUser(user=user)


class DeleteUser(graphene.Mutation):
    # 删除用户，仅将 is_active 设置为 False，没有从数据库删除

    user = graphene.Field(UserType)

    @login_required
    def mutate(self, info) -> 'DeleteUser':
        user = info.context.user
        user.is_active = False
        user.save()

        return DeleteUser(user=user)


class CreateDiary(graphene.Mutation):
    # 创建日记

    diary = graphene.Field(DiaryType)

    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    @login_required
    def mutate(self, info, title: str, content: str) -> 'CreateDiary':
        diary = info.context.user.diaries.create(title=title, content=content)

        return CreateDiary(diary=diary)


class UpdateDiary(graphene.Mutation):
    # 更新日记

    diary = graphene.Field(DiaryType)

    class Arguments:
        release_time = graphene.DateTime(required=True)
        title = graphene.String()
        content = graphene.String()

    @login_required
    def mutate(self, info, release_time: datetime.datetime, **kwargs) -> 'UpdateDiary':
        diary = info.context.user.diaries.get(release_time=release_time)
        updated = False
        if 'title' in kwargs:
            diary.title = kwargs['title']
            updated = True
        if 'content' in kwargs:
            diary.content = kwargs['content']
            updated = True
        if not updated:
            raise GraphQLError(str(ErrorMessage(
                code=update_diary_no_parameters_code,
                message=update_diary_no_parameters_message)))
        diary.save()

        return UpdateDiary(diary=diary)


class DeleteDiary(graphene.Mutation):
    # 删除日记

    diary = graphene.Field(DiaryType)

    class Arguments:
        release_time = graphene.DateTime(required=True)

    @login_required
    def mutate(self, info, release_time: datetime.datetime) -> 'DeleteDiary':
        diary = info.context.user.diaries.get(release_time=release_time)
        diary.delete()

        return DeleteDiary(diary=diary)


class Query(graphene.ObjectType):
    # 普通用户可以访问的字段
    user = graphene.Field(UserType, description='获取用户信息，普通用户可访问。')

    # staff 可以访问的字段
    users = graphene.List(UserType, description='获取所有用户的信息，员工用户可访问。')

    @login_required
    def resolve_user(self, info, **kwargs):
        return info.context.user

    @staff_member_required
    def resolve_users(self, info, **kwargs):
        return get_user_model().objects.all()


class Mutations(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field(description='获取 JWT Token，匿名用户即可访问。')
    verify_token = graphql_jwt.Verify.Field(description='查看 JWT Token 信息，普通用户即可访问。')
    refresh_token = graphql_jwt.Refresh.Field(description='刷新 JWT Token，普通用户即可访问。')
    revoke_token = graphql_jwt.Revoke.Field(description='撤销 JWT Token，普通用户即可访问。')

    # 用户相关操作
    create_user = CreateUser.Field(
        description='创建用户，匿名用户可访问。'
    )
    update_user = UpdateUser.Field(
        description='更新用户，普通用户可访问。'
    )
    delete_user = DeleteUser.Field(
        description='删除用户，普通用户可访问。'
    )

    # 日记相关操作
    create_diary = CreateDiary.Field(
        description='创建日记，如果没有则创建，普通用户可访问。'
    )
    update_diary = UpdateDiary.Field(
        description='更新日记，普通用户可访问。'
    )
    delete_diary = DeleteDiary.Field(
        description='删除日记，普通用户可访问。'
    )


schema = graphene.Schema(query=Query, mutation=Mutations)
