import flet as ft
from flet.controls.core import list_view

from UI import controller
from UI.alert import AlertManager
'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.dd = None
        self.dd1 = None
        self.list_view = None        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        self.dd = ft.Dropdown(label="Biblioteca", width=250)
        biblioteche = self.controller.get_biblioteche()

        self.dd.options.append(ft.DropdownOption(key="", text="all"))
        for b in biblioteche:
            self.dd.options.append(ft.DropdownOption(key=f"{b.id}", text=f"{b}"))

        self.dd1 = ft.Dropdown(label="Genere", width=250)
        generi = self.controller.get_generi()
        self.dd1.options.append(ft.DropdownOption(key="", text="all"))
        for g in generi:
            self.dd1.options.append(ft.DropdownOption(key=f"{g}", text=f"{g}"))
        row = ft.Row([self.dd, self.dd1],
                     alignment=ft.MainAxisAlignment.CENTER)
        bg_sel = ft.Button(content="Selected books",
                            on_click=self.controller.handler_bg_sel)
        # Sezione 3: Libri
        self.list_view = ft.ListView(expand=True, spacing=10, padding=10)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            row,

            ft.Divider(),
            bg_sel,

            # Sezione 3: Libri
            self.list_view
        )
        # list_view.controls.append(ft.Text("Ciao"))
        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()

