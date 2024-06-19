class Werknemer:
    def __init__(self, registratienummer):
        self.registratienummer = registratienummer

class Freelancer(Werknemer):
    def __init__(self, registratienummer, uurloon):
        super().__init__(registratienummer)
        self.uurloon = uurloon
        self.uren_gewerkt = 0

    def werkuren(self, uren):
        self.uren_gewerkt = uren

    def printverdiend(self):
        verdiend = self.uurloon * self.uren_gewerkt
        print(f"Werknemer: {self.registratienummer} verdient: {verdiend:.2f} Euro.")


class VasteKracht(Werknemer):
    def __init__(self, registratienummer, maandloon):
        super().__init__(registratienummer)
        self.maandloon = maandloon

    def printverdiend(self):
        print(f"Werknemer: {self.registratienummer} verdient: {self.maandloon:.2f} Euro.")


# Testprogramma voor Opdracht 1a
f = Freelancer(1, 25.75)         # werknemer 1 verdient 25.75 per uur
v = VasteKracht(2, 1873.53)      # werknemer 2 verdient 1873.53 per maand

f.werkuren(84)                   # werknemer 1 werkt (deze maand) 84 uren

print('Maand 1:')
f.printverdiend()
v.printverdiend()

f.werkuren(13.5)                 # werknemer 1 werkt (deze maand) 13.5 uren

print('Maand 2:')
f.printverdiend()
v.printverdiend()
