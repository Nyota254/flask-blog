from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Article


app = create_app('development')

manager = Manager(app)

manager.add_command('server',Server)
@manager.shell
def make_shell_context():
    return {'db' : db}


if __name__ == "__main__":
    manager.run()