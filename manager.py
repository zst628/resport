from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from info import create_app, db,models

# 创建 app，并传入配置模式：development / production
app = create_app('development')

manager = Manager(app)
# 数据库迁移
Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()