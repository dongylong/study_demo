创建python 3.7 venv
python -m venv ll_env

安装virtualenv
pip install --user virtualenv

创建虚拟环境
virtualenv ll_env
virtualenv ll_env --python=python3
激活虚拟环境
source ll_env/bin/activate
退出虚拟环境
deactivate

虚拟环境种：
安装Django
pip install Django==1.11

Django 中创建项目
django-admin.py startproject learning_log .

创建数据库
python manage.py migrate

创建的数据库
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Apply all migrations：应用所有的迁移
 ls
db.sqlite3      learning_logs    ll_env          manage.py

是否正确创建项目
python manage.py runserver
python manage.py runserver 8001 指定端口

创建应用程序
source ll_env/bin/activate
python manage.py startapp learning_app

# My apps
'learning_app',

激活模型
python manage.py makemigrations learning_app
python manage.py migrate

创建超级用户
python manage.py createsuperuser

迁移模型
python manage.py makemigrations learning_app
python manage.py migrate