# 接口小实验

## 简介

项目目录如下：

```
.                       // 当前目录: django-lab
├── interface_app       // 项目文件夹
│   ├── db.sqlite3
│   ├── holiday         // 节日查询应用接口
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py     // 接口视图对应的urls
│   │   └── views.py    // 定义了接口视图
│   ├── interface_app   // 项目配置
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py     // 项目整体对应的urls
│   │   └── wsgi.py
│   ├── manage.py
│   └── user_auth       // 注册及登录应用接口
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py 
│       ├── models.py   
│       ├── tests.py    
│       ├── urls.py     // 接口视图对应的urls
│       └── views.py    // 定义了接口视图
├── README.md           // 文档
└── requirements.txt    // 项目所需的python包

4 directories, 23 files

```

### 配置及运行

> 在WSL(Ubuntu 18.04 bionic [Ubuntu on Windows 10]) 下

配置时需要执行以下命令（Windows请根据venv文档修改虚拟环境启动方式）：

```bash
python3 -m venv env                                       # 建立虚拟环境
source env/bin/activate                                   # 如果不需要虚拟环境可以不执行这两条
pip install -r requirements.txt                           # 安装需求配置
python ./interface_app/manage.py migrate                  # 迁移数据库
python ./interface_app/manage.py runserver 127.0.0.1:8000 # 启动服务器
```

此时127.0.0.1的8000端口应当已经成功运行服务器

## 接口介绍

### 注册接口 (signup)

使用POST方法查询。

- **url:** `/user/signup`

- **参数:**
  
  - `username`: 字符串(最大长度100）
  
  - `password`: 字符串(最大长度100）

- **返回值:**

  - `status_code`: 一个整数，含义如下：
  
    - `0`: 注册成功，同时会注册成功的用户名

    - `1`: 用户名已存在，同时返回"username exists"信息

    - `2`: 未填写用户名，同时返回"username empty"信息

    - `3`: 未填写密码，同时返回"password empty"信息

    - `-1`: 未使用POST方法，同时返回"Please use POST method to login."信息

  - `error_info`: 在`status_code`不为0时返回如上所示的错误信息。

  - `username`: 字符串，返回注册成功的用户名。
  
### 登录接口 (login)

使用POST方法查询。

- **url:** `/user/login`

- **参数:**
  
  - `username`: 字符串(最大长度100）
  
  - `password`: 字符串(最大长度100）

- **返回值:**

  - `status_code`: 一个整数，含义如下：
  
    - `0`: 登录成功，同时会返回生成的token key值和登录成功的用户名

    - `1`: 密码错误，同时返回"password incorrect"信息

    - `2`: 未填写用户名，同时返回"username empty"信息

    - `3`: 未填写密码，同时返回"password empty"信息

    - `4`: 用户名不存在，同时返回"username not exist"信息

    - `-1`: 未使用POST方法，同时返回"Please use POST method to login."信息

  - `error_info`: 在`status_code`不为0时返回如上所示的错误信息。

  - `username`: 字符串，返回登录成功的用户名。
  
  - `token`: 字符串，登录成功时返回token key值。

### 查询节日接口 (holiday)

使用POST方法查询。

- **url:** `/holiday`

> 根据rest_framework对于token验证的规定，我们需要将Token放在发送包头部(Header)中进行身份验证。
> 
> 源码及注释如下：
> ```python
> class TokenAuthentication(BaseAuthentication):
>       """
>     Simple token based authentication.
> 
>     Clients should authenticate by passing the token key in the "Authorization"
>     HTTP header, prepended with the string "Token ".  For example:
> 
>         Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
>     """
> 
>     keyword = 'Token'
>     model = None
> ```

据此可以得出头部参数规则为：

- **Header 参数:**

  - `Authorization`: 字符串，格式为 `"Token " + token.key`，其中token.key为登录时返回的key值。 

- **参数 (body 参数):**

  - `date`: 字符串，格式为`YYYY-MM-DD`，（例：`2000-01-01`）

- **返回值:**

  - `status_code`: 数字，含义如下：

    - `0`: 查询成功，同时返回节日名称

    - `2`: 不存在参数date，返回"param date does not exist"信息

    - `3`: date格式错误，返回"error_info": "Date format invalid. Please provide format: YYYY-MM-DD"信息

    > 注：原先为1的位置由于题目要求(`如果这一天不是要求的三个节日，空的json格式的信息`)，返回空json，故删除。

  - `error_info`: 如上所示，返回对应`status_code`的信息

  - `holiday_name`: 返回对应节日（`"元旦"`、`"国庆节"`、`"圣诞节"`）