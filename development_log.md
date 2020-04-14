# EmailDiary 咕咕咕团队的不咕记录

- [队员开发日志](#队员开发日志)
- [版本控制](#版本控制)
- [争议排除](#争议排除)
- [推荐阅读](#推荐阅读)
- [组会记录](#组会记录)
  - [第八周](#第八周)

## 队员开发日志

- [陈一](https://gist.github.com/cycychenyi/86ded7116028fb96c244d69c2d355407)
- [张心蕊](https://gist.github.com/XinRuiiii/b3fe67a15d8660d44f1dbc3d506966e7)
- [牛冰冰](https://gist.github.com/niubingbing/056fbfe640b0a8ce901fc110aeab88cc)

**请大家先认真看完「不咕记录」，加上自己的开发日志链接，提交首次 PR。**

**请大家先认真看完「不咕记录」，加上自己的开发日志链接，提交首次 PR。**

**请大家先认真看完「不咕记录」，加上自己的开发日志链接，提交首次 PR。**

如果还没有内容，先提交空白文档链接，之后在该链接内进行更新，如果需要更换链接再次提交 PR 即可。

大家都走一遍流程，对以后提交代码的过程比较清晰。

## 版本控制

[Git 官方教程](https://git-scm.com/book/zh/v2)

1. 使用 Git 命令行或 GitHub Desktop 进行版本控制。

2. 贡献代码时，先 fork 到本地，再进行 PR 提交，可以 [通过 PR 同步团队仓库的更新](https://blog.csdn.net/qq1332479771/article/details/56087333)。（PR 我会认真审核，主要是希望大家规范一下编程风格。其实可以使用工具审核，但我还没学会，如果有人会请教下我哈。—— 陈一）

3. 每次开发一个功能或者修复一个 Bug 新建一个分支，在分支里进行开发。（如果你为了省事非得在 master 分支上开发我也没看不出来，不过建议使用分支开发。—— 陈一）

4. 切换分支的时候保持工作区和暂存区干净，即完成所有 add 和 commit 操作。如果使用 GitHub Desktop，则无需注意这个问题。

   工作区：本地文件系统。

   暂存区：已 add 但未 commit 的文件保存在暂存区。

5. Github 仓库采用 [压缩合并提交](https://help.github.com/cn/github/administering-a-repository/about-merge-methods-on-github#squashing-your-merge-commits)，开发时可以随意 commit，提交 PR 后 merge 只会保留一条 commit 记录。每完成一个完整的功能记得及时 merge，否则最后的版本控制里看不到中间的 commit。

6. 尽管有 .gitignore，但难免有漏网之鱼。每次 commit 时请注意查看文件的变动，不要提交临时文件和涉及隐私的文件。

7. 新建了一个 test 仓库以供测试。

## 争议排除

1. 数据验证由前端单独实现。
   - 邮箱有效性验证：参见 [维基](https://zh.wikipedia.org/wiki/電子郵件地址#规则)。
   - 密码复杂度检测：数字、小写字母、大写字母、半角标点至少包含两种，长度至少为 8 位。

2. 导出由前端单独实现。

   *注：导入由前端读取文件，将数据传给后端。*

3. 词云由前端单独实现。

## 推荐阅读

**通用**

- [EmailDiary 的错误代码](backend/backend/error_messages.py)
- [EmailDiary 的 GraphQL 参考示例](https://gist.github.com/cycychenyi/636a01657b4c48fc3e040a3306f0b626)
- [JSON Web Token 入门教程](https://www.ruanyifeng.com/blog/2018/07/json_web_token-tutorial.html)

**前端**

- [wired-element 文档](https://github.com/wiredjs/wired-elements)
- [wired-element 示例](https://wiredjs.com/showcase.html)
- [Vue 中文文档](https://cn.vuejs.org/v2/guide/)
  - 建议前端同学不要跟着文档用 HBuider X，统一使用 WebStorm 建立 Vue 项目
  - [WebStorm 中使用 Vue 入门教程]([https://blog.jetbrains.com/cn/2019/06/%E5%9C%A8-webstorm-%E4%B8%AD%E4%BB%A5-vue-js-%E6%9E%84%E5%BB%BA%E5%BA%94%E7%94%A8%E5%85%A5%E9%97%A8/](https://blog.jetbrains.com/cn/2019/06/在-webstorm-中以-vue-js-构建应用入门/))

**后端**

- [Django 文档](https://docs.djangoproject.com/zh-hans/3.0/)
- [GraphQL 官网](https://graphql.cn/)
- [Graphene-Django 官网](https://docs.graphene-python.org/projects/django/en/latest/)
- [Django GraphQL JWT 官网](https://django-graphql-jwt.domake.io/en/latest/)

## 组会记录

*注：如果图片太小，可以右键「在新标签页中打开图片」*

*再注：图片是透明的，关于深色模式下观看不便的问题请自行解决。*

#### 第八周

<div align="center"><img src="http://qn.cycychenyi.com/emaildiary/weekly-08.png" alt="weekly-08.png" /></div>