#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""错误代码和错误信息"""

"""与用户有关的错误以 3 开头"""

# 创建用户
invalid_email_code = 300
invalid_email_message = 'The email address is invalid!'
user_already_exist_code = 301
user_already_exist_message = 'The email address is already registered!'

# 更新用户
update_user_no_parameters_code = 302
update_user_no_parameters_message = 'Please pass in the field of the user that needs to be changed!'


"""与日记有关的错误以 4 开头"""

# 更新日记
update_diary_no_parameters_code = 400
update_diary_no_parameters_message = 'Please pass in the new title or content of the diary!'
