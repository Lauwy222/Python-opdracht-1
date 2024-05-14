class Werknemer():
    def __init__(self, WerknemerNr, Loon):
        self.WerknemerNr = WerknemerNr
        self.Loon = Loon
        self.verdiend = 0.0

    def geefnummer(self):
        return self.WerknemerNr

    def geefverdiensten(self):
        return self.verdiend

    def printverdiend(self):
        print(f'werknemer: {self.geefnummer()} verdient: {self.geefverdiensten(): 8.2f} Euro')

class Freelancer(Werknemer):
    def __init__(self, WerknemerNr, Loon):
        Werknemer.__init__(self, WerknemerNr, Loon)
    def werkuren(self, uren):
        self.verdiend = self.Loon * uren

class VasteKracht(Werknemer):
    def __init__(self, WerknemerNr, Loon):
        Werknemer.__init__(self, WerknemerNr, Loon)
        self.omzetten()

    def omzetten(self):
        self.verdiend = self.Loon

class Stukwerker(Werknemer):
    def __init__(self, WerknemerNr, Loon):
        Werknemer.__init__(self, WerknemerNr, Loon)
    def produceerstuks(self, stuks):
        self.verdiend = self.Loon * stuks

f = Freelancer(1, 25.75)  # werknemer 1 verdient 25.75 per uur
v = VasteKracht(2, 1873.53)  # werknemer 2 verdient (deze maand) 84 uur
s = Stukwerker(3, 1.05)
f.werkuren(84)
s.produceerstuks(1687)
print('Maand 1:')
f.printverdiend()
v.printverdiend()
s.printverdiend()
f.werkuren(13.5)
s.produceerstuks(0)
print('Maand 2:')
f.printverdiend()
v.printverdiend()
s.printverdiend()