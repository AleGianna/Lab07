from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO ():
    def __init__(self):
        pass

    def read_all_libri_from_db(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []

        query = "SELECT id, titolo, autore, genere, anno_pubblicazione, id_biblioteca FROM libro"  # Adatta le colonne al tuo DB
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)

        libri = []
        for row in cursor:
            libro = Libro(
                id=row["id"],
                titolo=row["titolo"],
                autore=row["autore"],
                genere=row["genere"],
                anno_pubblicazione=row["anno_pubblicazione"],
                id_biblioteca=row["id_biblioteca"],  # oppure la chiave esatta presente nel tuo DB
                # aggiungi gli altri campi se presenti nel DTO
            )
            libri.append(libro)

        cursor.close()
        cnx.close()
        return libri
