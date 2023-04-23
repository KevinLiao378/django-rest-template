# {{cookiecutter.project_name}}

{{ cookiecutter.description }}

---

## 安装依赖
```shell
# 开发环境
pip install -r requirenments/develop.txt
# 生产环境
pip install -r requirenments/production.txt
```
## 初始化
1. 配置环境变量。在项目根目录新建`.env`文件，写入：
    ```shell
    DEBUG=True
    DATABASE_URL=sqlite:///db.sqlite3
    ```
2. 迁移
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```
3. 创建管理员用户
    ```shell
    python manage.py createsuperuser
    ```
## 运行调试
```shell
python manage.py runserver
```
