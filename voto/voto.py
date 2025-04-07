from dataclasses import dataclass

@dataclass(order=True)
class Voto:
    materia: str
    punteggio: int
    data: str
    lode: bool

    #obbligatori
    def __eq__(self, other):  # nella creazione della materia abbiamo scelto come chiave la materia
        return self.materia == other.materia

    def __hash__(self):
        #return hash((self.materia, self.punteggio, self.lode))
        return hash(self.materia)

    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

    def copy(self):
        return Voto(self.materia, self.punteggio, self.data, self.lode)

