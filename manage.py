from app import create_app,db
from flask_script import Manager, Server
from app.models import User,Comment
from flask_migrate import Migrate,MigrateCommand

app=create_app('test')

manager=Manager(app)
manager.add_command('server',Server)
#create a migrate command
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)
#use the manager shell decorator to access the shell on the command line
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Comment=Comment)

@manager.command
def test():
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
if __name__=='__main__':
    manager.run()