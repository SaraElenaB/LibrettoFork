import mysql.connector

from dao.dbConnect import DBConnect
from voto.voto import Voto


class LibrettoDAO:

    #def __init__(self):
        #self.dbConnect = DBConnect() --> avendo fatto @classmethod non lo devo più scrivere così

    def getAllVoti(self):
        # cnx = mysql.connector.connect( user="root",
        #                                password="rootroot1",
        #                                host="127.0.0.1",
        #                                database="libretto")

        #cnx= self.dbConnect.getConnection() --> se fosse stato un metodo per le istanze
        cnx = DBConnect.getConnection() #--> dato che è un metodo di classe
        cursor = cnx.cursor( dictionary=True)

        query = """select * from voti"""
        cursor.execute(query)

        res= []
        for row in cursor:
            # materia= row['materia']
            # punteggio= row['punteggio']
            # data= row['data']
            # lode= row['lode']
            # v=Voto(materia, punteggio, data, lode)
            # ris.append(v)

            #dato che c'è lode che è un bool ma noi stiamo stampando con str, facciamo così:
            if row["lode"]== "False":
                res.append( Voto( row["materia"], row['punteggio'], row['data'].date(), False)) #.date() per prendere solo l'ora e non anche l'ora
            else:
                res.append(Voto(row["materia"], row['punteggio'], row['data'].date(), True))

        cnx.close()
        return res

    def addVoto(self, voto: Voto):
        # cnx= mysql.connector.connect( user="root",
        #                               password="rootroot1",
        #                               host="127.0.0.1",
        #                               database="libretto")

        cnx = DBConnect.getConnection()
        cursor = cnx.cursor( dictionary=True)
        query= ("insert into voti(materia, punteggio, data, lode) values (%s, %s, %s, %s)") #%s, parametro che passiamo da fuori, non sappiamo i valori
        cursor.execute(query, (voto.materia, voto.punteggio, voto.data, str(voto.lode) ) ) #database accetta stringe
        cnx.commit() #perchè modifica il database
        cnx.close()

    def hasVoto(self, voto: Voto):
        # cnx = mysql.connector.connect( user="root",
        #                                password="rootroot1",
        #                                host="127.0.0.1",
        #                                database="libretto")

        cnx = DBConnect.getConnection()
        cursor = cnx.cursor()
        query = """select * from voti v where v.materia = %s """
        cursor.execute(query, (voto.materia,) )
        res = cursor.fetchall() #altrimenti da errore che non hai usato i risultati
        return len(res)>0 #quindi ci dice se c'è o no il voto


#test
if __name__=="__main__":
    mydao = LibrettoDAO()
    mydao.getAllVoti()
