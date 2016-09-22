from flask import Flask, render_tempalte
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    bootstrap
