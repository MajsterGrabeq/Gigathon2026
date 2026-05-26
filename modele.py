class Postac:
    def __init__(self, imie: str, x: int, y: int, jedzenie: int):
        self.imie = imie
        self.x = x
        self.y = y
        self.jedzenie = jedzenie
        self.punkty = 0
        self.hp = 100

class Mapa:
    def __init__(self, rozmiar: int):
        self.rozmiar = rozmiar

class Krypta:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y