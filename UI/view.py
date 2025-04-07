import datetime

import flet as ft

class View:
    def __init__(self, page: ft.Page):
        self._student = None
        self._titolo = None
        self._txtOut = None
        self._btnIn = None
        self._txtIn = None
        self._controller = None   #serve solo per non scordarsi niente, te lo dice già il programma
        self._page = page

    def setController(self, c):
        self._controller = c

    def _fillDDvoto(self):
        for i in range(18,31):
            self._ddVoto.options.append(ft.dropdown.Option(str(i)))
        self._ddVoto.options.append(ft.dropdown.Option("30L"))

    def loadInterface(self):
        #metodo in cui carichiamo tutti i controlli dell'interfaccia

        #self._page.bgcolor = "white" --> colore di backround
        self._titolo= ft.Text("libretto voti",
                              color="blue", size=24)
        self._student = ft.Text(value=self._controller.getStudent(),
                                color="brown") #chiamo un metodo perchè non so chi sia

        row1 = ft.Row([self._titolo],
                      alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self._student] ,
                      alignment=ft.MainAxisAlignment.END)

        #RIGA DEI CONTROLLI
        self._txtIn = ft.TextField(label="Nome esame",
                                   hint_text="Inserisci il nome dell'esame",
                                   width=300) #txtInNome
        self._ddVoto = ft.Dropdown(label="Voto",
                                   width=120) #il dopdown vuole uan lista di azioni non una stringa -->
                                              # molto spesso le info del dropdown le sappiamo dopo,
        self._fillDDvoto()

        self._db = ft.DatePicker(
                first_date= datetime.datetime(2022, 1, 1),
                last_date= datetime.datetime(2026, 12, 31),
                on_change= lambda e: print(f"Giorno selezionato: {self._db.value}"),
                on_dismiss= lambda e: print("Data non selezionata")
                )

        self._btnCall= ft.ElevatedButton("Pick date",
                                         icon=ft.Icons.CALENDAR_MONTH,
                                         on_click=lambda _: self._page.open(self._db))
                                        #di fatto qui e non lo usiamo, ma la convenzione dice che dobbiamo mettere un underscore

        self._btnAdd= ft.ElevatedButton("Add date",
                                        on_click=self._controller.handleAggiungi())

        self._btnPrint= ft.ElevatedButton("Print date",
                                          on_click=self._controller.handleStampa())

        row3 = ft.Row( [self._txtIn, self._ddVoto, self._btnCall, self._btnAdd, self._btnPrint],
                       alignment=ft.MainAxisAlignment.CENTER)

        self._txtOut= ft.ListView(expand=True )
        self._page.add( row1, row2, row3, self._txtOut)

    @property
    def txtOut(self):
        return self._txtOut







