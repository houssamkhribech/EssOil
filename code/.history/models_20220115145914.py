import os
from flask_sqlalchemy import SQLAlchemy


def ApplicationConfig(app):
    app.secret_key = 'Clé secrète'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
    app.config['SESSION_TYPE'] = 'sqlalchemy'
    db = SQLAlchemy(app)
    app.config['SESSION_SQLALCHEMY'] = db 