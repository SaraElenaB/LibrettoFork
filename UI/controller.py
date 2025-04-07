from scuola import Student
from UI.view import View
from voto.modello import Libretto #dal package voto importa voto
import flet as ft

from voto.voto import Voto

class Controller:
    def __init__(self, v: View):
        self._view = v
        self._student= Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")
        self._model = Libretto(self._student, [])

    # def _fillLibretto(self): --> improprio dovrebbe stare nel modello
    #     v1 = Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)
    #     self._model.append(v1)
    #     v2 = Voto("Babbanologia", 30, "2022-02-12", False)
    #     self._model.append(v2)
    #     self._model.append(Voto("Pozioni", 21, "2022-02-14", False))
    #     v4 = Voto("Trasfigurazioni", 22, "2022-02-12", False)
    #     self._model.append(v4)

    def handleAggiungi(self, e): #e
        """
        Raccoglie tutte le info per creare un nuovo voto, crea oggetto Voto, fa append sul libretto
        :param e:
        :return:
        """
        nome = self._view._txtInNome.value
        if nome=="":
            self._view.txtOut.controls.append( ft.Text("Attenzione. Il campo nome non può essere vuoto", color="red"))
            self._view._page.update()
            return

        punti = self._view._ddVoto.value
        if punti is None:
            self._view.txtOut.controls.append( ft.Text("Attenzione. Selezionare un punteggio valido", color="red"))
            self._view._page.update()
            return

        data = self._view._db.value
        if data is None:
            self._view.txtOut.controls.append( ft.Text("Attenzione. Selezionare una data.", color="red"))
            self._view._page.update()
            return

        if punti=="30L":
            self._model.append(nome, 30, f"{data.year}-{data.month}-{data.day}", True)
        else:
            voto = Voto(nome, int(punti), f"{data.year}-{data.month}-{data.day}", False)
            self._model.append(voto)

        self._view._txtOut.controls.append( ft.Text("Voto correttamente aggiunto.", color="green"))


    def handleStampa(self, e):
        print("handle stampa")
        self._view._txtOut.controls.append( ft.Text( str(self._model), color="black" )) #modifica l'interfaccia e quindi devo modificarla
        self._view._page.update()
        #non puoi solo return str(self._model) perche non sai dove stampa

    def getStudent(self):
        """
        Metodo che restituisce informazioni dello studente usando il metodo __str__ --> lo prendi dal modello
        :return:
        """
        return str(self._student)



