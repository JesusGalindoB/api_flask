from flask import Flask 
from views import api
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/jprojects/web_projects/flask_api/app/api.db'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


if __name__ == '__main__':
    db.init_app(app)
    app.register_blueprint(api)
    app.run()