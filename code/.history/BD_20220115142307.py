
import sqlite3
import time

##
## Fonctions d'aide à la manipulation de bases de données
##
	
def OpenDatabase():
    # Ouverture d'une base de données SQLite, en réessayant jusqu'à ce
    # que le fichier contenant la base de données soit disponible
    while True:
        try:
            return sqlite3.connect('.sqlite3')
        except Exception as e:
            time.sleep(0.1)
            continue   # Nouvel essai après 100 ms

def ExecuteDatabase(db, sql, args = []):
    cursor = db.cursor()
    try:
        cursor.execute(sql, args)
        results = cursor.fetchall()
        cursor.close()
        return results
    except Exception as e:
        # On s'assure de fermer le curseur même en cas d'échec
        cursor.close()
        return None

def CloseDatabase(db):
    # Ne jamais oublier de refermer la base de données SQLite, sinon
    # plus personne ne peut s'y connecter !
    db.commit()
    db.close()
	
