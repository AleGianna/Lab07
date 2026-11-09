import flet as ft
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def get_biblioteche(self):
        biblioteche = self._model.get_biblioteche()
        return biblioteche
    def get_generi(self):
        generi = self._model.get_generi()
        return generi

    # CALLBACKS DROPDOWN
    def handler_bg_sel(self):
        b = self._view.dd.value
        g = self._view.dd1.value


        result = self._model.get_libri_filtrati(b,g)
        self._view.list_view.controls.clear()
        self._view.list_view.controls.append(ft.Text(f"selected: {len(result)}"))
        for l in result:
            self._view.list_view.controls.append(ft.Text(f"{l}"))
        self._view.update()

    # AZIONE: MOSTRA LIBRI
