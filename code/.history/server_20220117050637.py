#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import *

app = Flask(__name__)
db = ApplicationConfig(app)            # Configuration de la session côté serveur pour plus de sécurité => seul le session_id sera stocké dans le coockie
server_session = Session(app)
#db.create_all()
bcrypt = Bcrypt(app)
#Bootstrap(app)


# Déclaration des enums
class Role(Enum):
    ADMIN = 0
    STUDENT = auto()
    USER = auto()
   
class PlantType(Enum):
    LAVENDER = auto()
    ORANGE_BLOSSOM = auto()
    EUCALYPTUS = auto()
    PEPPER_MINT = auto()

class Storage(Enum):
    FRIDGE = auto()
    BOX = auto()
    CABINET = auto()


def ReadFile(path):
    with open(path, 'rb') as f:
        return f.read()

@app.route('/')
def redirection():
    return redirect('login', code = 302)

@app.route('/home')
def index():
    username = session.get('username')
    if not username:
        return redirect('login', code = 302)
    return ReadFile('index.html')

@app.route('/monitoring')
def monit():
    username = session.get('username')
    if not username:
        return redirect('login', code = 302)
    return ReadFile('templates/monitoring.html')

@app.route('/control')
def control():
    username = session.get('username')
    if not username:
        return redirect('login', code = 302)
    return ReadFile('templates/control.html')

@app.route('/administration')
def administration():
    username = session.get('username')
    if not username:
        return redirect('login', code = 302)
    return ReadFile('templates/administration.html')

@app.route('/database')
def data():
    username = session.get('username')
    if not username:
        return redirect('login', code = 302)
    return ReadFile('templates/data.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'username' in session:
            return redirect('home', code = 302)
        else:
            return ReadFile('templates/login.html')
    elif request.method == 'POST':
        query = json.loads(request.get_data().decode('utf-8'))
        state, DB_results = checklog(query['username'])                                                 # Récupération des données de l'utilisateur dans la db
        if ( state == True and bcrypt.check_password_hash(DB_results[0][6], query['password'])):        # Vérification du mot de passe
            session['username'] = DB_results[0][5]
            """session['user_id'] = DB_results[0][0]
            session['role'] = DB_results[0][1]
            session['matricule'] = DB_results[0][2]"""
            print("mot de passe correct")
            return redirect('home', code = 302)
        else:
            abort(400)  
    else: 
        abort(400)

@app.route('/logout', methods = [ 'POST'] )
def doLogout():
    if 'username' in session:
        del session['username']
        session.clear()
    return redirect('login', code = 302)
   

@app.route('/add-user', methods=['POST', 'GET'])
def addUserServ():
    if request.method == 'GET':
        return ReadFile('templates/addUser.html')
    elif request.method == 'POST':
        newUser = json.loads(request.get_data().decode('utf8'))
        newUser['role'] = Role[newUser['role']].value
        newUser['password'] = bcrypt.generate_password_hash(newUser['password']).decode('utf-8')        # hashage du mot de passe
        return addUser(newUser)
    else:
        abort(400)

@app.route('/add-experiment', methods = [ 'POST', 'GET' ])
def addExprimentServ():
    if request.method == 'GET':
        return ReadFile('templates/addExp.html')
    elif request.method == 'POST':
        data = json.loads(request.get_data().decode('utf8'))
        data['plantType'] = PlantType[data['plantType']].value                                          # Stockage d'un nombre au lieu d'une chaine => LAVENDER = 1 
        data['storage'] = Storage[data['storage']].value
        experiment = {
            'uid': data['uid'],
            'waterVolume': int(data['waterVolume']),
            'hydrolatVolume': int(data['hydrolatVolume']),
            'pressure': int(data['pressure']),
            'temperature': int(data['temperature']),
            'plantType': int(data['plantType']),
            'plantRef': data['plantRef'],
            'plantMass': int(data['plantMass']),
            'oilMass': float(data['oilMass']),
            'storage': int(data['storage']),
            'storageDate': data['storageDate'],
            'storageCondition': data['storageCondition'],
        }
        sample = {
            'plantType': experiment['plantType'],
            'plantRef': experiment['plantRef'],
            'plantMass': experiment['plantMass'],
            'oilMass': experiment['oilMass'],
            'storage': experiment['storage'],
            'storageDate': experiment['storageDate'],
            'storageCondition': experiment['storageCondition'],
        }
        sampleId = addSample(sample)                                                                  
        userId = getUserID(session["username"])

        if sampleId[0] == True and userId[0] == True:
            return addExp(experiment, sampleId[1], userId[1])
        else:
            return(400)
    else: 
        abort(400)

# Renvoyer une liste de tous les enums
@app.route('/get-all-listbox')
def getListbox():
    data = [[],[],[]]
    for role in Role:
        data[0].append(role.name)
    for plantType in PlantType:
        data[1].append(plantType.name) 
    for storage in Storage:
        data[2].append(storage.name)
    return json.dumps(data)


@app.route('/get-experiments')
def getExperimentsServ():
    experiments= getExperiments()

    exp_list = []  # car on ne peut pas modifier des Tuples
    for experiment in experiments:
        row = list(experiment)
        row[5] = PlantType(row[5]).name
        row[9] = Storage(row[9]).name
        exp_list.append(row)

    return json.dumps(exp_list)
   
@app.route('/get-users')
def getUsersServ():
    users = getUsers()
    users_list = []  # car on ne peut pas modifier des Tuples
    for user in users:
        row = list(user)
        row[1] = Role(row[1]).name
        users_list.append(row)

    return json.dumps(users_list)

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

@app.route('/bootstrap_dist/css/bootstrap.min.css')
def bootstrap():
    return ReadFile('bootstrap_dist/css/bootstrap.min.css')

"""@app.route('/inituser')
def init():
    pw_hash1 = bcrypt.generate_password_hash('Houssam').decode('utf-8')    # hashage du mot de passe
    pw_hash2 = bcrypt.generate_password_hash('Youssef').decode('utf-8')    # hashage du mot de passe
    Inituser(pw_hash1, pw_hash2)
    return "ok"

"""

# Communication avec L'ESP32
@app.route('/switch-state', methods=['GET', 'POST'])
def switchState():
    if request.method == 'POST':
        switchesState = json.loads(request.get_data().decode('utf8')) 
        return updateSwitchState(switchesState)
    elif request.method == 'GET':
        return json.dumps(getSwitchesState())
    else:
        abort(400)

@app.route('/post-sensor-from-ESP32', methods=['POST'])
def post():
    #data = json.loads(request.get_data().decode('utf8'))                                                                                                                         # dictionnaire qui contient les données des capteurs
    table_tank_temp = [("1", 22), ("2", 25), ("3", 28), ("4",30), ("5", 40), ("6", 50), ("7", 60), ("8",65), ("9",70), ("10", 90), ("11", 93), ("12", 94)]                       # température dans la cuve en °C - fréquence 1 éch/min
    table_cooling_temp = [("1", 20), ("2", 22), ("3", 23), ("4",24), ("5", 25), ("6", 28), ("7", 30), ("8",32), ("9", 33), ("10", 34), ("11", 35), ("12", 38)]                   # température du liquide de refroidissement en °C
    table_tank_pressure = [("1", 1000), ("2", 950), ("3", 900), ("4",24), ("5", 850), ("6", 800), ("7", 800), ("8",800), ("9", 33), ("10", 800), ("11", 800), ("12", 800)]       # pression dans la cuve en mBar
    
    labels = [row[0] for row in table_tank_temp]
    values = [row[1] for row in table_tank_temp]
    render_template("monitoring.html", labels, values)
    return 'ok'

@app.route('/initswitch')
def 
if __name__ == '__main__':
    #Inituser()
    Initialize()
    #app.run(host='0.0.0.0', port= 8090)
    app.run(debug=True)