import mysql.connector

class DBConnect:

    @classmethod #dice al programma che questo è un metodo di classe non di istanza
    def getConnection(self):

        try:
            cnx = mysql.connector.connect(user="root",
                                          password="rootroot1",
                                          host="127.0.0.1",
                                          database="libretto")
        except mysql.connector.Error as err:
            print("Non riesco a collegarmi al database")
            print(err)
            return None

