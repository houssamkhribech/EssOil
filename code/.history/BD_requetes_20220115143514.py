from BD import *

def Initialize():
    # Initialisation de la base de données
    db = OpenDatabase()
            
    ExecuteDatabase(db, 'CREATE TABLE IF NOT EXISTS users' +
                    '(user_id INTEGER PRIMARY KEY AUTOINCREMENT, role INTEGER, matricule TEXT, lastname TEXT NOT NULL, firstname TEXT NOT NULL, mail TEXT NOT NULL, pass TEXT NOT NULL)')
    ExecuteDatabase(db, 'CREATE TABLE IF NOT EXISTS samples' +
                    '(sample_id INTEGER PRIMARY KEY AUTOINCREMENT, plant_type INTEGER, plant_ref TEXT, plant_mass INTEGER, oil_mass FLOAT, storage, storage_date DATE, storage_condition TEXT)')
    ExecuteDatabase(db, 'CREATE TABLE IF NOT EXISTS experiments' +
                    '(uid TEXT, water_volume INTEGER NOT NULL, hydrolat_volume INTEGER NOT NULL, pressure INTEGER NOT NULL, temperature INTEGER NOT NULL, sample_id INTEGER, user_id INTEGER, ' +
                    'PRIMARY KEY (uid), ' +
                    'FOREIGN KEY (sample_id) REFERENCES samples(sample_id), FOREIGN KEY (user_id) REFERENCES users(user_id) )')
    CloseDatabase(db)

def Inituser():
    #Initialisation d'utilisateur
    db = OpenDatabase()
    
    req = 'INSERT INTO users (role, matricule, lastname, firstname, mail, pass) values (0, "B2200145", "Khribech", "Houssam", "H.Khribech@HE.com", "Houssam")'
    ExecuteDatabase(db, req)
    req = 'INSERT INTO users (role, matricule, lastname, firstname, mail, pass) values (0, "B2200211", "Tiberkanine", "Youssef" , "Y.Tiberkanine@HE.com", "Youssef")'
    ExecuteDatabase(db, req)
    CloseDatabase(db)

def addUser(newUser):
    #Initialisation d'utilisateur
    print(newUser)
    db = OpenDatabase()
    req = 'INSERT INTO users (role, matricule, lastname, firstname, mail, pass) values (?, ?, ?, ?, ?, ?)'
    ExecuteDatabase(db, req,[newUser['role'],newUser['matricule'],newUser['lastname'],newUser['firstname'], newUser['mail'], newUser['password']])
    CloseDatabase(db)
    return 'ok'

def addSample(sample):
    print(sample)
    db = OpenDatabase()
    req = 'INSERT INTO samples (plant_type, plant_ref, plant_mass, oil_mass, storage, storage_date, storage_condition) values (?, ?, ?, ?, ?, ?, ?)'
    results, sample_id = ExecuteDatabase2(db, req,[sample['plantType'], sample['plantRef'], sample['plantMass'], sample['oilMass'], sample['storage'], sample['storageDate'], sample['storageCondition']])
    if sample_id != None:
        CloseDatabase(db)
        return True, sample_id
    CloseDatabase(db)
    return False, sample_id

def addExp(experiment, sampleID, userID):
    print(userID)
    db = OpenDatabase()
    req = 'INSERT INTO experiments (uid, water_volume, hydrolat_volume, pressure, temperature, sample_id, user_id) values (?, ?, ?, ?, ?, ?, ?)'
    ExecuteDatabase(db, req,[experiment['uid'], experiment['waterVolume'],experiment['hydrolatVolume'], experiment['pressure'], experiment['temperature'], sampleID, userID])
    CloseDatabase(db)
    return "ok"

def getUserID(mail):
    db = OpenDatabase()
    userID = ExecuteDatabase(db, 'SELECT user_id FROM users WHERE mail = ?', [mail])
    if userID != []:
        CloseDatabase(db)
        return True, userID[0][0]
    CloseDatabase(db)
    return False, userID


def getUser(userId):
    db = OpenDatabase()
    user = ExecuteDatabase(db, 'SELECT user_id, role, matricule, lastname, firstname, mail FROM users Where user_id = ?',(userId))
    
    CloseDatabase(db)
    return user

def getSample(sampleId):
    db = OpenDatabase()
    sample = ExecuteDatabase(db, 'SELECT * FROM users Where sample_id = ?',(sampleId))
    CloseDatabase(db)
    return sample
	
def getExperimentsOnly():
    db = OpenDatabase()
    experiments_table = ExecuteDatabase(db, 'SELECT * FROM experiments')
    CloseDatabase(db)
    return experiments_table

def getExperiments():
    db = OpenDatabase()
    experiment = ExecuteDatabase(db, 'SELECT uid, experiments.water_volume, experiments.hydrolat_volume, experiments.pressure, experiments.temperature, samples.plant_type, samples.plant_ref, samples.plant_mass, samples.oil_mass, samples.storage, samples.storage_date, samples.storage_condition FROM experiments INNER JOIN samples ON experiments.sample_id = samples.sample_id')
    CloseDatabase(db)
    return experiment

def getSamples():
    db = OpenDatabase()
    samples_table = ExecuteDatabase(db, 'SELECT * FROM samples')
    CloseDatabase(db)
    return samples_table

def getUsers():
    db = OpenDatabase()
    users_table = ExecuteDatabase(db, 'SELECT user_id, role, matricule, lastname, firstname, mail FROM users')
    CloseDatabase(db)
    return users_table

def checklog(mail):
    # Vérifie la présence de l'adresse mail dans la base de donnée
    db = OpenDatabase()
    info = ExecuteDatabase(db, 'SELECT matricule,lastname,firstname,role,pass FROM users WHERE mail = ?', (mail,))
    if info != []:
        CloseDatabase(db)
        return True, info
    CloseDatabase(db)
    return False, -1, "", "", "", -1 #role -1 = erreur (temporaire)



