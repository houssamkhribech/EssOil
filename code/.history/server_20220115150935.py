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
#BASE_PATH = os.path.dirname(os.path.realpath(__file__)) #répertoire

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
    return ReadFile('index.html')

@app.route('/nav.css')
def navBar():
    return ReadFile('static/css/nav.css')

@app.route('/signin.css')
def loginStyle():
    return ReadFile('static/css/signin.css')

@app.route('/app.js')
def javascript():
    return ReadFile('app.js')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'username' in session:
            return redirect('home', code = 302)
        else:
            return ReadFile('templates/login.html')
    else:
        query = json.loads(request.get_data().decode('utf-8'))
        state, bdinfos = checklog(query['username'])
        print(bd)
        # Vérification du mot de passe
        if ( state == True and bcrypt.check_password_hash(query['password'], bdinfos[0][6])):
            session['username'] = query['username']
            session['user_id'] = bdinfos[0][0]
            session['role'] = bdinfos[0][1]
            session['matricule'] = bdinfos[0][2]
            return 'ok'
        else:
            abort(400)  

@app.route('/logout', methods = [ 'POST','GET'] )
def logout():
    if 'username' in session:
        session.clear()
    return redirect('login')
   
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


@app.route('/lib/chart.js')
def charJS():
    return ReadFile('lib/chart.js')


if __name__ == '__main__':
    #Inituser()
    Initialize()
    app.run(debug=True)