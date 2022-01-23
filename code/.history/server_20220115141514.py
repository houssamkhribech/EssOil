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

ApplicationConfig(app)            # configuration de la session côté serveur pour plus de sécurité
server_session = Session(app)


# Déclara
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
        # Vérification du mot de passe
        if ( state == True and query['password'] == bdinfos[0][4]):
            session['username'] = query['username']
            return json.dumps({
            'matricule' : bdinfos[0][0],
            'lastname' : bdinfos[0][1],
            'firstname' : bdinfos[0][2],
            'role' : bdinfos[0][3]
            })
        else:
            abort(400)  # Bad request

@app.route('/logout', methods = [ 'POST','GET'] )
def logout():
    if 'username' in session:
        del session['username']
    return redirect('login')
   





@app.route('/lib/chart.js')
def charJS():
    return ReadFile('lib/chart.js')


if __name__ == '__main__':

    Initialize()
    app.run(debug=True)