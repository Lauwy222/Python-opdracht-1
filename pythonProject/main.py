class Werknemer:
    def __init__(self, registratienummer):
        self.registratienummer = registratienummer

    def printverdiend(self, maand):
        raise NotImplementedError("Deze methode moet worden overschreven door subclasses")


class Freelancer(Werknemer):
    def __init__(self, registratienummer, uurloon, uren_per_maand):
        super().__init__(registratienummer)
        self.uurloon = uurloon
        self.uren_per_maand = uren_per_maand

    def printverdiend(self, maand):
        verdiend = self.uurloon * self.uren_per_maand[maand - 1]
        print(f"Werknemer: {self.registratienummer} verdient: {verdiend:.2f} Euro.")


class VasteKracht(Werknemer):
    def __init__(self, registratienummer, maandloon):
        super().__init__(registratienummer)
        self.maandloon = maandloon

    def printverdiend(self, maand):
        print(f"Werknemer: {self.registratienummer} verdient: {self.maandloon:.2f} Euro.")


# Testprogramma voor Opdracht 1a
uren_per_maand_freelancer = [43.26, 6.95]  # Voorbeeld uren voor de eerste en tweede maand
maandloon_vastekracht = 1873.53

werknemers = [
    Freelancer(registratienummer=1, uurloon=50, uren_per_maand=uren_per_maand_freelancer),
    VasteKracht(registratienummer=2, maandloon=maandloon_vastekracht)
]

for maand in range(1, 3):  # Voor de eerste en tweede maand
    print(f"Maand {maand}:")
    for werknemer in werknemers:
        werknemer.printverdiend(maand)
