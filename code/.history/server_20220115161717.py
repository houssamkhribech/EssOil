#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import abort
from flask import Flask, redirect, request, url_for, session
from flask_session import Session
from flask_bcrypt import Bcrypt
import json
from BD_requetes import *
from enum import Enum, auto
from models import *


app = Flask(__name__)
bcrypt = Bcrypt(app)
ApplicationConfig(app)            # Configuration de la session côté serveur pour plus de sécurité
server_session = Session(app)

#db.create_all()

# Déclaration des enums
class Role(Enum):
    ADMIN = auto()
    USER = auto()
    STUDENT = auto()

class PlantType(Enum):
    LAVENDER = auto()

class Storage(Enum):
    FRIDGE = auto()
    CLOSET = auto()



def ReadFile(path):
    with open(path, 'rb') as f:
        return f.read()

@app.route('/')
def redirection():
    return redirect('login', code = 302)

@app.route('/home')
def index():
    username = session.get("username")
    if not username:
        return redirect('login', code = 302)
    return ReadFile('index.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'username' in session:
            return redirect('home', code = 302)
        else:
            return ReadFile('templates/login.html')
    elif request.method == 'POST':
        query = json.loads(request.get_data().decode('utf-8'))
        state, DB_results = checklog(query['username'])
        # Vérification du mot de passe
        if ( state == True and bcrypt.check_password_hash(DB_results[0][6], query['password'])):
            session['username'] = DB_results[0][5]
            """session['user_id'] = DB_results[0][0]
            session['role'] = DB_results[0][1]
            session['matricule'] = DB_results[0][2]"""
            return redirect('home', code = 302)
        else:
            abort(400)  
    else: 
        abort(400)

@app.route('/logout', methods = [ 'POST'] )
def doLogout():
    if 'username' in session:
        session.clear()
    return "ok"
   
@app.route('/hello')
def say_hell():
    username = session.get("username")
    if not username:
        return 'unauthorized'
    return "Hello"



"""@app.route('/inituser')
def init():
    pw_hash1 = bcrypt.generate_password_hash('Houssam').decode('utf-8')    # hashage du mot de passe
    pw_hash2 = bcrypt.generate_password_hash('Youssef').decode('utf-8')    # hashage du mot de passe
    Inituser(pw_hash1, pw_hash2)
    return "ok"""

@app.route('/nav.css')
def navBar():
    return ReadFile('static/css/nav.css')

@app.route('/signin.css')
def loginStyle():
    return ReadFile('static/css/signin.css')

@app.route('/app.js')
def javascript():
    return ReadFile('app.js')

@app.route('/lib/chart.js')
def charJS():
    return ReadFile('lib/chart.js')


if __name__ == '__main__':
    #Inituser()
    Initialize()
    app.run(debug=True)