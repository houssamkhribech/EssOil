import os
from os import abort
from flask import Flask, redirect, request, url_for, session, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bcrypt import Bcrypt
import json
from BD_requetes import *
from enum import Enum, auto
from flask_bootstrap import Bootstrap
def ApplicationConfig(app):
    app.secret_key = 'Clé secrète'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
    app.config['SESSION_TYPE'] = 'sqlalchemy'
    db = SQLAlchemy(app)
    app.config['SESSION_SQLALCHEMY'] = db 
    


