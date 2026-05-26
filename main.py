import turtle
from modele import Postac, Mapa, Krypta
from mechanika import losuj_trase, powrot_do_krypty, generuj_raport

turtle.setup(600, 600)
turtle.bgcolor("#1a1a1a")

while True:
    print("=" * 60)
    print("                SYMULATOR EKSPEDYCJI: FALLOUT ")
    print("=" * 60)
    print("Witaj Nadzorco! Twój zwiadowca opuści bezpieczną Kryptę, aby")
    print("eksplorować niebezpieczne pustkowia w poszukiwaniu łupu.")
    print("Twoim zadaniem będzie zarządzanie jego powrotem, tak aby nie")
    print("umarł oraz zebranie jak największej ilości kapsli,")
    print("przed skończeniem się jedzenia")
    print("-" * 60)

    imie = input("\n-> Podaj imię mieszkańca Krypty: ").strip()[:25]
    if not imie:
        imie = "Bezimienny"

    print("\nPodaj teraz ilość jedzenia z jaką wyślesz swojego mieszkańca")
    print("Ilość jedzenia działa jak poziom trudności, im więcej tym łatwiej (default: 100)")
    
    try:
        jedzenie = int(input("-> Podaj ilość jedzenia z jaką wyślesz swojego mieszkańca: "))
    except ValueError:
        jedzenie = 100
        print("[System]: Błędna wartość! Ustawiono domyślne: 100")

    try:
        rozmiar = int(input("-> Podaj rozmiar mapy (int): "))
    except ValueError:
        rozmiar = 250
        print("[System]: Błędna wartość! Ustawiono domyślnie: 250")

    mapa = Mapa(rozmiar)

    print(f"Podaj koordynaty krypty, gdzie -{rozmiar} <= x & y <= {rozmiar}")

    while True:
        try:
            x = int(input("X: "))
            y = int(input("Y: "))

            if -rozmiar <= x <= rozmiar and -rozmiar <= y <= rozmiar:
                krypta = Krypta(x, y)
                break
            else:
                print("Poza mapą!")
        except ValueError:
            print("Podaj liczby!")

    start_jedzenie = jedzenie

    postac = Postac(imie, x, y, jedzenie)

    #pod nowa gra
    turtle.clear()
    turtle.title(f"Fallout: Monitor Ekranu Ekspedecyjnego - {postac.imie}")
    turtle.speed(0)

    #rysowanie krypty
    turtle.penup()
    turtle.goto(krypta.x - 5, krypta.y - 5)
    turtle.pendown()
    turtle.color("#00aaff")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()

    #granice mapy
    turtle.penup()
    turtle.goto(-mapa.rozmiar, -mapa.rozmiar)
    turtle.pendown()
    turtle.color("#444444")
    for i in range(4):
        turtle.forward(mapa.rozmiar * 2)
        turtle.left(90)


    turtle.penup()
    turtle.goto(postac.x, postac.y)
    turtle.shape("circle")
    turtle.shapesize(0.5)
    turtle.color("green")
    turtle.speed(3)

    # ROZGRYWKA
    kierunki = {"E": 0, "NE": 45, "N": 90, "NW": 135, "W": 180, "SW": 225, "S": 270, "SE": 315}
    w_kryptie = False
    kroki = 0
    przyczyna_konca = ""

    while postac.hp > 0 and not w_kryptie:
        kroki += 1
        print(f"\n======================= KROK {kroki} =======================")
        print(f"STATUS: {postac.imie} | HP: {postac.hp}/100 | Jedzenie: {postac.jedzenie} | Kapsli: {postac.punkty}")
        print(f"Aktualna pozycja: ({round(postac.x, 1)}, {round(postac.y, 1)})")
        print("-" * 60)
        print("Co chcesz zrobić?")
        print(" 1. Idź dalej eksplorować pustkowia")
        print(" 2. Zarządź powrót do Krypty")
        
        while True:
            akcja = input("Twoja decyzja (1/2): ").strip()
            if akcja in ["1", "2"]:
                break
            print("Podaj proszę poprawną opcję (wpisz 1 lub 2)")
        
        if akcja == "1":
            print(f"Dostępne kierunki: {', '.join(kierunki.keys())}")
            wybrany_kierunek = input(f"Gdzie ma iść {postac.imie}?: ").strip().upper()
            
            if wybrany_kierunek in kierunki:
                losuj_trase(kierunki[wybrany_kierunek], postac, mapa)
            else:
                print("[System]: Nieznany kierunek, postać kręci się w kółko.")
                
        elif akcja == "2":
            powrot_do_krypty(postac, krypta)
            w_kryptie = True 
            if postac.hp > 0:
                przyczyna_konca = "Bezpieczny powrót do Krypty"
            else:
                przyczyna_konca = "Zmarł z wycieńczenia w drodze powrotnej"

    if postac.hp <= 0 and not w_kryptie:
        przyczyna_konca = "Zginął podczas eksploracji pustkowi"

    
    generuj_raport(postac, start_jedzenie, mapa.rozmiar, kroki, przyczyna_konca)

    #nowa gra
    ponowna_gra = ""
    while ponowna_gra not in ["T", "N"]:
        ponowna_gra = input("\nCzy chcesz zagrać jeszcze raz? (T/N): ").strip().upper()
            
    if ponowna_gra != "T":
        print("\nDziękuję za grę, Nadzorco! Do zobaczenia w bezpieczniejszych czasach.")
        break

turtle.done()