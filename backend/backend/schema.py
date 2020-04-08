# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
import json

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
        # filter_fields = {'name': ['exact', 'icontains', 'istartswith'],
        #                  'customer': ['exact', 'icontains', 'istartswith']}


class DiaryType(DjangoObjectType):
    class Meta:
        model = Diary


class CreateUser(graphene.Mutation):
    # 创建用户

    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        name = graphene.String(required=True)

    def mutate(self, info, email, password, name):
        if User.objects.filter(email=email):
            raise GraphQLError(str(ErrorMessage(
                code=USER_ALREADY_EXIST_CODE,
                message=USER_ALREADY_EXIST_MESSAGE)))
        user = get_user_model()(
            email=email,
            password=password,
            name=name
        )
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
    def mutate(self, info, **kwargs):
        user = info.context.user
        if 'password' in kwargs:
            user.set_password(kwargs['password'])
        if 'name' in kwargs:
            user.name = kwargs['name']
        user.save()

        return UpdateUser(user=user)


class CreateDiary(graphene.Mutation):
    # 创建日记

    diary = graphene.Field(DiaryType)

    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    @login_required
    def mutate(self, info, title, content):
        diary = info.context.user.diaries.create(title=title, content=content)

        return CreateDiary(diary=diary)


class DeleteUser(graphene.Mutation):
    # 删除用户，仅将 is_active 设置为 False，没有从数据库删除

    user = graphene.Field(UserType)

    @login_required
    def mutate(self, info, release_time):
        user = info.context.user
        user.is_active = False
        user.save()

        return DeleteUser(user=user)


class UpdateDiary(graphene.Mutation):
    # 更新日记

    diary = graphene.Field(DiaryType)

    class Arguments:
        release_time = graphene.DateTime(required=True)
        title = graphene.String()
        content = graphene.String()

    @login_required
    def mutate(self, info, release_time, **kwargs):
        diary = info.context.user.diaries.get(release_time=release_time)
        if 'title' in kwargs:
            diary.title = kwargs['title']
        if 'content' in kwargs:
            diary.content = kwargs['content']
        diary.save()

        return UpdateDiary(diary=diary)


class DeleteDiary(graphene.Mutation):
    # 删除日记

    diary = graphene.Field(DiaryType)

    class Arguments:
        release_time = graphene.DateTime(required=True)

    @login_required
    def mutate(self, info, release_time):
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
    token_auth = graphql_jwt.ObtainJSONWebToken.Field(description='获取 JWT Token，普通用户即可访问。')
    verify_token = graphql_jwt.Verify.Field(description='查看 JWT Token 信息，普通用户即可访问。')
    refresh_token = graphql_jwt.Refresh.Field(description='刷新 JWT Token，普通用户即可访问。')
    revoke_token = graphql_jwt.Revoke.Field(description='撤销 JWT Token，普通用户即可访问。')

    create_user = CreateUser.Field(
        description=f'创建用户，匿名用户可访问。\n'
                    '如果该邮箱已注册，返回错误代码 {USER_ALREADY_EXIST_CODE}。'
    )
    update_user = UpdateUser.Field(
        description='更新用户，普通用户可访问。'
    )
    delete_user = DeleteUser.Field(
        description='删除用户，普通用户可访问。'
    )
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
