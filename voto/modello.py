import operator
from dataclasses import dataclass
import flet as ft
from dao.dao import LibrettoDAO

cfuTot = 180
#----------------------------------------------------------------------------------------------------------------------------------------
class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti
        self.dao = LibrettoDAO()
        self.fillLibretto() #lo devi chiamare da qualche parte altrimenti è come se non facessi nulla

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def fillLibretto(self):
        allEsami = self.dao.getAllVoti()
        for e in allEsami:
            self.append(e) #prende l'append spiegato dopo
                           #fa l'append su un libretto locale

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def append(self, voto): # duck!
        if( (self.hasVoto(voto) is False) and (self.hasConflitto(voto) is False) ):
            self.voti.append(voto)
            if not LibrettoDAO.hasVoto(voto):
                self.dao.addVoto(voto) #non riscrive se il voto c'è lo abbiamo già
        else:
            raise ValueError("Voto already exists")

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario} \n"
        for v in self.voti:
            mystr += f"{v} \n"
        return mystr

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def __len__(self):
        return len(self.voti)

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def copy(self):
        """
        Crea una nuova copia del libretto
        :return:
        """
        nuovo = Libretto(self.proprietario.copy(), voti=[])
        for v in self.voti:
            nuovo.append(v.copy())
        return nuovo

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def calcolaMedia(self):
        """"
        restituisce la media dei voti attualmente presenti nel libretto
        :return: valore numerico della media oppure ValueError nel caso in cui la lista fosse vuota
        """
        #media= sommaVoti/numEsami
        if len(self.voti) == 0:
            raise ValueError("Attenzione lista esami vuota! ")

        votiSemplificato = [v.punteggio for v in self.voti]     #lista vuota che riempi svolgendo il ciclo for
        return sum(votiSemplificato)/len(votiSemplificato)

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def getVotiByPunti(self, punti, lode): #voti --> lista
        """"
        se è un dataclass c'è ne freghiamo?? questa è la comodità del dataclass
        se la classe degli oggetti contenuti in self.voti fosse stata definita come un @dataclass di Python, si sarebbe potuto evitare di scrivere
        manualmente alcuni metodi, tra cui il costruttore (__init__), il metodo di confronto (__eq__), e anche la rappresentazione (__repr__)
        :param punti: variabile di tipo intero che rappresenta il punteggio
        :param lode: booleano che indica se è presente la lode
        :return: lista voti
        """
        votiFiltrati=[]
        for v in self.voti:
            if v.punteggio == punti and v.lode==lode:
                votiFiltrati.append(v)
        return votiFiltrati

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def getVotobyName(self, nome): #voto --> oggetto
        """
        restituisce un oggetto voto il cui campo materia è uguale a nome
        :param nome: stringa che indica il nome della materia
        :return: oggetti di tipo Voto, oppure None in caso di voto non trovato
        """
        for v in self.voti:
            if v.materia == nome:
                return v

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def hasVoto(self, voto):
        """
        Questo metodo verifica se il libretto continiene già il voto: 2 voti sono = se hanno stesso campo materia e punteggio. Punteggio: punteggio + lode (2 campi)
        :param voto: istanza dell'ogg di tipo Voto
        :return: True se voto è già presente oppure False altrimenti
        """
        for v in self.voti:
            #metodo 1: if v==voto --> stesso oggetto
            #metodo 2: controlla i campi, non l'oggetto
            if (v.materia==voto.materia and v.punteggio==voto.punteggio and v.lode==voto.lode):
                return True #esce appena ne trova 1
        return False

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def hasConflitto(self, voto):
        """
        Questo metodo controlla che il voto "voto" non presents un conflitto con i voti già presenti nel libretto.
        Conflitto=stessa materia ma diverso punteggio(voto, lode)
        :param voto: istanza di oggetto Voto
        :return: True se voto è in conflitto oppure False altrimenti
        """
        for v in self.voti:
            if( (v.materia==voto.materia) and not (v.punteggio==voto.punteggio and v.lode==voto.lode) ):
                return True
        return False

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def creaLibrettoMigliorato(self): #metodo defactoring --> crea nuove classi dell'istanza stessa
        """
        Crea un nuovo oggetto libretto in cui i voti sono migliorati secondo la seguente logica:
           -18<voto<24: aggiungo +1,
           -24<voto<29: aggiungo +2,
           - voto=29:   aggiungo +1,
           - voto=30:   rimane 30,
        :return: nuovo Libretto
        """
        # newLibretto = Libretto(self.proprietario, voti=[] )  #copia la lista, non prendere solo i voti --> se modifichi i voti, modifichi anche i vecchi
        # for v in self.voti:
        #     #newLibretto.append(Voto( v.materia, v.punteggio, v.data, v.lode ) ) #così è completamente indipendete -->
        #     newLibretto.append(v.copy())

        newLibretto = self.copy()
        for v in newLibretto.voti:
            if 18<=v.punteggio<24:
                v.punteggio +=1
            elif 24<=v.punteggio<29:
                v.punteggio +=2
            elif v.punteggio==29:
                v.punteggio +=30

        return newLibretto

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def sortByMateria(self):
        """
        1°: creo 2 metodi che stampano, uno che prima ordina e poi stampa
        2° creo 2 metodi che ordinano la lista di self, un unico metodo di stampa
        3° creo 2 metodi che si fanno una copia autonoma della lista --> ordinano --> altro metodo si occupererà di stampare
        4° creo una shallow copy di self.voti (agisco solo sulla lista, non sugli oggetti)
        :return:
        """
        #self.voti.sort( key=estraiMateria) #key: ordina in base alla funzione passata come chiave
        self.voti.sort( key=operator.attrgetter("materia")) #voto.materia

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def sortByVoto(self):
        pass

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def creaLibOrdinatoPerMateria(self):
        """
        Crea un oggetto Libretto e lo ordina per materia
        :return: nuova istanza oggetto Libretto
        """
        newLibMateria = self.copy()
        newLibMateria.sortByMateria() #--> def la funzione
        return newLibMateria

        # newLibMateria = self.copy()
        # newLibMateria.voti.sort( key=lambda v: v.materia) #lambda=sto definendo una funzione di voto --> ovvero ordina per materia
        # return newLibMateria

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def creaLibOrdinatoPerVoto(self):
        """
        Crea un oggetto Libretto e lo ordina per voto
        :return: nuova istanza oggetto Libretto
        """
        newLibVoto = self.copy()
        newLibVoto.voti.sort( key=lambda v: (v.punteggio, v.lode), reverse=True) #ordinami --> criterio di ordinamento è una tupla, controlla prima il primo campo e poi il secondo
        return newLibVoto

    # ----------------------------------------------------------------------------------------------------------------------------------------
    def cancellaInferiori(self, punteggio):
        """
        1°: metodo agisce sul libretto corrente, eliminando tutti  i voti inferiori al parametro passato
        :param punteggio: int+bool
        :return:
        """
        #modo 1: --> non va bene perchè ogni ogni volta che controlla una posizione, aumenta e passa alla successiva quindi non controlla tutto
        # for i in range(len(self.voti)):
        #     if self.voti[i].punteggio < punteggio:
        #         self.voti.pop(i)

        #modo 2: --> inefficiente
        # for i in range(len(self.voti)):
        #     if self.voti[i].punteggio < punteggio:
        #         self.voti.remove(i)

        #modo 3:
        # newLibretto = []
        # for v in self.voti:
        #     if v.punteggio >= punteggio:
        #         newLibretto.append(v)
        # self.voti = newLibretto

        #modo 3.0:
        #newLibretto=[]
        self.voti=[ v for v in self.voti if v.punteggio >= punteggio]
        #newLibretto = self.voti
        #return newLibretto

# ----------------------------------------------------------------------------------------------------------------------------------------
def estraiMateria(voto):
    """
    Questo metodo restituisce il campo materia dell'oggetto voto
    :param voto: istanza classe voto
    :return: str materia
    """
    return voto.materia

#-----------------------------------------------------------------------------------------------------------------------------------------
# def testVoto():
#     print("Ho usato Voto in maniera standalone")
#     v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
#     v2 = Voto("Pozioni", 30, "2022-02-17", True)
#     v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)
#     print(v1)
#
#     mylib = Libretto(None, [v1, v2])
#     print(mylib)
#     mylib.append(v3)
#     print(mylib)
#     print((ft.Text(mylib)))

#-----------------------------------------------------------------------------------------------------------------------------------------
# if __name__ == "__main__":
#     testVoto()


# class Voto:
#     def __init__(self, materia, punteggio, data, lode):
#         if  punteggio == 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = lode
#         elif punteggio < 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = False
#         else:
#             raise ValueError(f"Attenzione, non posso creare un voto con punteggio {punteggio}")
#     def __str__(self):
#         if self.lode:
#             return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
#         else:
#             return f"In {self.materia} hai preso {self.punteggio} il {self.data}"
