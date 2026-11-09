from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''



class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()
        self.libri = self._libro_dao.read_all_libri_from_db()
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        dao = BibliotecaDAO()
        biblioteche = dao.read_biblioteche_from_db()
        return biblioteche

    # --- LIBRI ---
    def get_libri_filtrati(self,b, g):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        libri_filtrati = []
        if b == "":
            b=None
        if g == "":
            g=None

        if b is None:
            if g is None:
                for l in self.libri:
                        libri_filtrati.append(l)
                return libri_filtrati
            else:
                for l in self.libri:
                    if str(l.genere) == str(g):
                        libri_filtrati.append(l)
                return libri_filtrati
        else:
            if g is None:
                for l in self.libri:
                    if str(l.id_biblioteca) == str(b):
                        libri_filtrati.append(l)
                return libri_filtrati
            else:
                for l in self.libri:
                    if str(l.genere) == str(g) and str(l.id_biblioteca) == str(b):
                        libri_filtrati.append(l)
                return libri_filtrati












    def get_generi(self):
        """Estrae i generi univoci direttamente dai libri salvati in memoria."""
        # Prende l'attributo genere da ogni libro ed elimina i duplicati con set()
        generi = set(libro.genere for libro in self.libri if libro.genere is not None)
        return sorted(list(generi))
    # --- BIBLIOTECHE ---

