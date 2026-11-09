from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass




    def read_biblioteche_from_db(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection to database established")

            #query ="SELECT * FROM trip"
            query ="SELECT id,nome,indirizzo FROM biblioteca"
            cursor = cnx.cursor()
            cursor.execute(query)
            # Leggo tutto dal cursore in una variabile results
            # result = cursor.fetchall()
            result = []
            for row in cursor:
                biblioteca = Biblioteca(*row)
                result.append(biblioteca)

            cursor.close()
            cnx.close()
            print("biblioteche read from database")
            return result