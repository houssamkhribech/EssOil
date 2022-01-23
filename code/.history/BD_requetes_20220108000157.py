from BD import *

def Initialize():
    # Initialisation de la base de données
    db = OpenDatabase()
            
    ExecuteDatabase(db, 'CREATE TABLE IF NOT EXISTS users' +
                    '(user_id INTEGER PRIMARY KEY AUTOINCREMENT, role INTEGER, lastname TEXT NOT NULL, firstname TEXT NOT NULL, email TEXT NOT NULL, pass TEXT NOT NULL)')
    ExecuteDatabase(db, 'CREATE TABLE IF NOT EXISTS samples' +
                    '(sample_id INTEGER PRIMARY KEY AUTOINCREMENT, plant_type INTEGER, plant_ref TEXT, plant_mass INTEGER, oil_mass INTEGER, storage INTEGER, storage_date DATE, storage_condition TEXT)')
    ExecuteDatabase(db, 'CREATE TABLE IF NOT EXISTS experiments' +
                    '(uid TEXT, water_volume INTEGER NOT NULL, hydrolat_volume INTEGER NOT NULL, pressure INTEGER NOT NULL, temperature INTEGER NOT NULL, sample_id INTEGER, matricule INTEGER, ' +
                    'PRIMARY KEY (uid), ' +
                    'FOREIGN KEY (sample_id) REFERENCES samples(sample_id), FOREIGN KEY (matricule) REFERENCES users(matricule) )')

    CloseDatabase(db)
#abort(400)

def Inituser():
    #Initialisation d'utilisateur
    db = OpenDatabase()
    req = 'INSERT INTO users (role, lastname, firstname, email, pass) values (1, "Khribech", "Houssam", "H.Khribech@HE.com", "Houssam")'
    ExecuteDatabase(db, req)
    req = 'INSERT INTO users (role, lastname, firstname, email, pass) values (1, "Tiberkanine", "Youssef" , "Y.Tiberkanine@HE.com", "Youssef")'
    ExecuteDatabase(db, req)
    CloseDatabase(db)

def checklog(email):
    # Vérifie la présence de l'adresse mail dans la base de donnée
    db = OpenDatabase()
    info = ExecuteDatabase(db, 'SELECT user_id,lastname,firstname,role,pass FROM users WHERE email = ?', (email,))
    if info != []:
        CloseDatabase(db)
        return True, info
    CloseDatabase(db)
    return False, -1, "", "", "", -1 #role -1 = erreur (temporaire)


"""def addExperiment(experiment):
    db = OpenDatabase()
    ExecuteDatabase(db, 'INSERT INTO sample VALUES(?,?,?,?,?,?,?)', [ experiment['plantType'], experiment['plantRef'], experiment['plantMass'], experiment['oilMass'], experiment['storage'], experiment['storageDate'], experiment['storageCondition'] ])
    CloseDatabase(db)
    return 'ok'
"""

def addExperiment(experiment):
    db = OpenDatabase()
    ExecuteDatabase(db, 'INSERT INTO samples VALUES(?,?,?,?,?,?,?)', [ "0", 'too get', '250', '5', '0', '10022020', 'ok' ])
    CloseDatabase(db)
    return 'ok'
#get

#Add

#Update

#Delete






# Ancienne requetes 
def getLessons(usertype, userid):
    db = OpenDatabase()
    if usertype == 'Student':
        lessons = ExecuteDatabase(db, 'SELECT learning.lesson_id,lessons.name FROM learning INNER JOIN lessons ON learning.lesson_id = lessons.lesson_id WHERE student_id = ? ORDER BY name', [ userid ]) 
    else:
        lessons = ExecuteDatabase(db, 'SELECT lesson_id,name FROM lessons WHERE teacher_id = ? ORDER BY name', [ userid ])
    CloseDatabase(db)
    return lessons

def getTests(userid, lessonid):
    db = OpenDatabase()
    tests = ExecuteDatabase(db, 'SELECT name,score,max_score FROM tests WHERE student_id = ? AND lesson_id = ? ORDER BY name', [ userid, lessonid ])
    CloseDatabase(db)
    return tests

def addtest(test):
    db = OpenDatabase()
    ExecuteDatabase(db, 'INSERT INTO tests VALUES(?,?,?,?,?)', [ test['name'], test['student_id'], test['lesson_id'], test['score'], test['max_score'] ])
    CloseDatabase(db)
    return 'ok'

def getTeachersStudents(lesson_id):
    db = OpenDatabase()
    students_id = ExecuteDatabase(db, 'SELECT learning.student_id, students.lastname, students.firstname FROM learning INNER JOIN students ON learning.student_id = students.student_id WHERE lesson_id = ? ORDER BY students.lastname, students.firstname',  [ lesson_id ] )
    CloseDatabase(db)
    return students_id

#old
def getTeachers():
    db = OpenDatabase()
    teachers = ExecuteDatabase(db, 'SELECT teacher_id,lastname,firstname FROM teachers ORDER BY lastname,firstname') #ORDER BY lastname,firstname
    CloseDatabase(db)
    return teachers
def getStudentsAll():
    db = OpenDatabase()
    students = ExecuteDatabase(db, 'SELECT student_id,lastname,firstname FROM students ORDER BY lastname,firstname') #ORDER BY lastname,firstname
    CloseDatabase(db)
    return students

def getStudents(student_id):
    db = OpenDatabase()
    student = ExecuteDatabase(db, 'SELECT lastname,firstname FROM student  WHERE student_id=?,', student_id) #ORDER BY lastname,firstname
    CloseDatabase(db)
    return student

def update(test):
    db = OpenDatabase()
    ExecuteDatabase(db,'UPDATE tets set score = ? WHERE name = ? AND student_id = ? AND lesson_id = ?', [ test['score'], test['name'], test['student_id'], test['lesson_id'] ])
    CloseDatabase(db)
    return 'ok'