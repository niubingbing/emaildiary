## EmailDiary 咕咕咕团队的不咕记录

- [版本控制](#版本控制)

- [争议排除](#争议排除)

## 队员开发日志

- [陈一](https://gist.github.com/cycychenyi/86ded7116028fb96c244d69c2d355407)

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

4. 切换分支的时候保持工作区和暂存区干净，即完成所有 add 和 commit 操作。

   工作区：本地文件系统。

   暂存区：已 add 但未 commit 的文件保存在暂存区。

5. Github 仓库采用 [压缩合并提交](https://help.github.com/cn/github/administering-a-repository/about-merge-methods-on-github#squashing-your-merge-commits)，开发时可以随意 commit，提交 PR 后 merge 只会保留一条 commit 记录。每完成一个完整的功能记得及时 merge，否则最后的版本控制里看不到中间的 commit。

6. 新建了一个 test 仓库以供测试。

## 争议排除

1. 数据验证由前端单独实现。
   - 邮箱有效性验证：参见 [维基](https://zh.wikipedia.org/wiki/電子郵件地址#规则)。
   - 密码复杂度检测：数字、小写字母、大写字母、半角标点至少包含两种，长度至少为 8 位。

2. 导出由前端单独实现。

   *注：导入由前端读取文件，将数据传给后端。*

3. 词云由前端单独实现。

## 推荐阅读

**通用**

- [EmailDiary 的 GraphQL 参考示例](https://gist.github.com/cycychenyi/636a01657b4c48fc3e040a3306f0b626)
- [JSON Web Token 入门教程](https://www.ruanyifeng.com/blog/2018/07/json_web_token-tutorial.html)

**前端**

**后端**

- [Django 文档](https://docs.djangoproject.com/zh-hans/3.0/)
- [GraphQL 官网](https://graphql.cn/)
- [Graphene-Django 官网](https://docs.graphene-python.org/projects/django/en/latest/)
- [Django GraphQL JWT 官网](https://django-graphql-jwt.domake.io/en/latest/)