from flask_script import Manager
from bluelog.models import db

from flask_migrate import Migrate,MigrateCommand

from bluelog import create_app


app = create_app()
manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
    manager.run()



#python qy.py db init 初始化会生成migrate文件夹

#python qy.py db migrate 生成迁移文件

#python qy.py db upgrade 更新数据库字段

#如果后几次更新数据库，只需要执行后面两步，因为第一次已经创建文件夹完成。