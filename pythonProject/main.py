class werknemer():
    def __init__(self, functie, salaris, uren):
        self.functie = functie
        self.salaris = salaris
        self.uren = uren


class Freelancer(werknemer):
    def werkuren(self, uren):
        self.uren = uren

    def printverdiend(self):
        pass


class VasteKracht(werknemer):
    def printverdiend(self):
        pass


f = Freelancer(1, 25.75)
v = VasteKracht(2, 1873.53)

f.werkuren(84)

print('Maand 1:')
f.printverdiend()
v.printverdiend()

f.werkuren(13.5)

print('Maand 2:')
f.printverdiend()
v.printverdiend()
