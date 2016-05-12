from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_webpack import Webpack

# webpack = Webpack()

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/meta_fb?charset=utf8mb4'
app = Flask(__name__)
db = SQLAlchemy(app)

settings = {
    'DEBUG': True,
    # 'WEBPACK_MANIFEST_PATH': './build/manifest.json',
    'SQLALCHEMY_DATABASE_URI' : SQLALCHEMY_DATABASE_URI,
    'SQLALCHEMY_TRACK_MODIFICATIONS' : True

}

app.config.update(settings)
# webpack.init_app(app)

from app import views