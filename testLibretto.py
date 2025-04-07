from scuola import Student
from voto.modello import Libretto, Voto

Harry = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")
myLib = Libretto(Harry, [])

v1 = Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)
v2 = Voto("Babbanologia", 30, "2022-02-12", False)
myLib.append( Voto( "Pozioni", 21, "2022-02-14", False))
v4 = Voto("Trasfigurazioni", 22, "2022-02-12", False)
v5 = Voto("Bacchette", 23, "2022-02-12", False)
v6 = Voto("Incantesimi", 24, "2022-02-12", False)
v7 = Voto("Patronus", 25, "2022-02-12", False)
v8 = Voto("Storia della magia", 26, "2022-02-12", False)
v9 = Voto("Piante stregate", 27, "2022-02-12", False)
v10 = Voto("Economia della stregonieria", 28, "2022-02-12", False)

myLib.append(v1)
myLib.append(v2)
myLib.append(v4)
myLib.append(v5)
myLib.append(v6)
myLib.append(v7)
myLib.append(v8)
myLib.append(v9)
myLib.append(v10)

myLib.calcolaMedia()

votiFiltrati = myLib.getVotiByPunti(23, False)
print(votiFiltrati[0])
#print(votiFiltrati[0])  #stampa il __str__
#print(votiFiltrati) stampa tutto

votoPozioni = myLib.getVotobyName("Pozioni")
if votoPozioni is None:
    print("Attenzione, non esiste nessun voto per quella materia! ")
else:
    print(votoPozioni)

print("---HA GIA IL VOTO: ---")
print(myLib.hasVoto(v1))
print(myLib.hasVoto(Voto("Difesa contro le arti oscure", 25, "2022-01-30", False))) #uguale a v1 ma riscritto
print(myLib.hasVoto(Voto("Aritmazia", 30, "2023-20-07", False )))

print("---HA CONFLITTO: ---")
print(myLib.hasConflitto(Voto("Difesa contro le arti oscure", 18, "2022-01-30", False)))

print("---MODIFICO APPEND: ---")
myLib.append(Voto("Aritmazia 2.0", 30, "2023-20-07", False ))                     #non succede niente
#myLib.append(Voto("Difesa contro le arti oscure", 25, "2022-01-30", False))       #raise ValueError

print("---NUOVO LIBRETTO: ---")
print("Libretto originario:------------------------------------------------------------------------------- ")
print(myLib)
print("Libretto aggiornato:------------------------------------------------------------------------------- ")
newLib = myLib.creaLibrettoMigliorato()
print(newLib)
print("Libretto originario 2.0:------------------------------------------------------------------------------- ")
print(myLib)

print("---NUOVO LIBRETTO ORDINATO MATERIA: ---")
ordinato = myLib.creaLibOrdinatoPerMateria()
print(ordinato)

print("---NUOVO LIBRETTO ORDINATO VOTO: ---")
ordinato2 = myLib.creaLibOrdinatoPerVoto()
print(ordinato2)

print("---LIBRETTO CANCELLANDO I VOTI INFERIORI: ---")
ordinato3 = myLib.creaLibOrdinatoPerVoto()
ordinato3.cancellaInferiori(24) #restituisce una nuova lista di voti filtrata --> prima gli dai la lista poi la filtra
print(ordinato3)


