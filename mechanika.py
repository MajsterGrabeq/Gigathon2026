import math
import random
import turtle
from modele import Postac, Mapa, Krypta

def event(postac: Postac):
    event_type = random.randint(1, 3)
    
    #Bandyta
    if event_type == 1:
        print("\nWytropił cię Bandyta!")
        print("Możesz podjąć walkę (szansa na kapsle, ale tracisz HP) lub uciekać")
        print(" 1. Walcz")
        print(" 2. Uciekaj")
        while True:
            decyzja = input("Twoja decyzja (1/2): ").strip()
            if decyzja in ["1", "2"]:
                break
            print("Podaj proszę poprawną opcję (wpisz 1 lub 2)")

        if decyzja == "1":
            damage = random.randint(5, 35)
            bonus_pkt = random.randint(20, 50)
            postac.hp -= damage
            if postac.hp < 0:
                postac.hp = 0
            else:
                print(f"Wygrywasz walkę z bandytą tracąc {damage} HP i zyskując {bonus_pkt} kapsli.")
            postac.punkty += bonus_pkt

        elif decyzja == "2":
            czy_oberwal = random.randint(1, 3)
            if czy_oberwal == 1:
                damage = random.randint(5, 30)
                postac.hp -= damage
                if postac.hp < 0: 
                    postac.hp = 0
                print(f"Uciekłeś! Jednak w trakcie ucieczki oberwałeś dodatkowo {damage} HP.")
            else:
                print("Bierzesz nogi za pas i uciekasz bez szwanku!")

    #Szczurek
    elif event_type == 2:
        print("\nDrogę zastępuje ci Kretoszczur!")
        print("Możesz podjąć walkę (szansa na jedzenie, ale tracisz HP) lub uciekać")
        print(" 1. Walcz")
        print(" 2. Uciekaj")
        while True:
            decyzja = input("Twoja decyzja (1/2): ").strip()
            if decyzja in ["1", "2"]:
                break
            print("Podaj proszę poprawną opcję (wpisz 1 lub 2)")

        if decyzja == "1":
            damage = random.randint(5, 25)
            bonus_jedzenie = random.randint(20, 30)
            postac.hp -= damage
            if postac.hp < 0:
                postac.hp = 0
            else:
                print(f"Wygrywasz walkę z Kretoszczurem tracąc {damage} HP i zyskując {bonus_jedzenie} jedzenia.")
            postac.jedzenie += bonus_jedzenie
            
        elif decyzja == "2":
            czy_oberwal = random.randint(1, 4)
            if czy_oberwal == 1:
                damage = random.randint(5, 15)
                postac.hp -= damage
                if postac.hp < 0: 
                    postac.hp = 0
                print(f"Uciekłeś! Jednak w trakcie ucieczki oberwałeś dodatkowo {damage} HP.")
            else:
                print("Bierzesz nogi za pas i uciekasz bez szwanku!")

    #Skarb
    elif event_type == 3:
        print("\nTrafiasz na stary, zamknięty schron Rad-Techu (Skarb)!")
        print("Zamki są zardzewiałe. Możesz spróbować je wyważyć, ale istnieje ryzyko pułapki.")
        print(" 1. Otwórz schron")
        print(" 2. Zostaw i idź dalej")
        while True:
            decyzja = input("Twoja decyzja (1/2): ").strip()
            if decyzja in ["1", "2"]:
                break
            print("Podaj proszę poprawną opcję (wpisz 1 lub 2)")

        if decyzja == "1":
            szansa = random.random()
            if szansa < 0.5:
                bonus_pkt = random.randint(40, 80)
                postac.punkty += bonus_pkt
                print(f"\nSukces! W środku był nienaruszony przedwojenny sejf. Zyskujesz {bonus_pkt} kapsli!")
            elif szansa < 0.6:
                bonus_jedzenie = random.randint(20, 40)
                postac.jedzenie += bonus_jedzenie
                print(f"\nZnalazłeś skrzynkę starych, sproszkowanych racji żywnościowych! Zyskujesz +{bonus_jedzenie} jedzenia.")
            else:
                obrazenia = random.randint(10, 25)
                postac.hp -= obrazenia
                if postac.hp < 0: 
                    postac.hp = 0
                print(f"\nWyważając drzwi, uruchomiłeś starą pułapkę wybuchową! Tracisz {obrazenia} HP.")
        elif decyzja == "2":
            print("\n[Wynik]: Decydujesz się nie ryzykować urwania rąk. Idziesz dalej.")

def losuj_trase(kierunek_stopnie: float, postac: Postac, mapa: Mapa):
    min_odleglosc = mapa.rozmiar * 0.1
    max_odleglosc = mapa.rozmiar * 0.25
    wylosowana_odleglosc = random.uniform(min_odleglosc, max_odleglosc)

    radiany = math.radians(kierunek_stopnie)
    start_x = postac.x
    start_y = postac.y

    cel_ostateczny_x = start_x + wylosowana_odleglosc * math.cos(radiany)
    cel_ostateczny_y = start_y + wylosowana_odleglosc * math.sin(radiany)

    jednostki_na_krok = 5 
    ilosc_krokow = max(1, int(wylosowana_odleglosc / jednostki_na_krok))

    print(f"\n[Wyprawa]: {postac.imie} planuje marsz w linii prostej")

    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()

    czy_bylo_ostrzezenie = False
    przerwano_marsz = False

    for i in range(1, ilosc_krokow + 1):
        if postac.jedzenie <= 0 and not czy_bylo_ostrzezenie:
            print(f"[Alert]: Brak jedzenia uniemożliwia dalszy marsz! Kontynuowanie podróży zada obrażenia.")
            czy_bylo_ostrzezenie = True

        procent_drogi = i / ilosc_krokow
        nowe_x = start_x + (cel_ostateczny_x - start_x) * procent_drogi
        nowe_y = start_y + (cel_ostateczny_y - start_y) * procent_drogi

        if abs(nowe_x) > mapa.rozmiar or abs(nowe_y) > mapa.rozmiar:
            print("[Alert]: Doszliśmy do końca mapy! Przerywanie marszu przed granicą.")
            break
        
        if postac.jedzenie > 15:
            turtle.pencolor("#00ff00")
        elif postac.jedzenie > 0:
            turtle.pencolor("#ffaa00")
        else:
            turtle.pencolor("#ff0000")
            
        turtle.goto(nowe_x, nowe_y)

        postac.x = nowe_x
        postac.y = nowe_y
        
        if postac.jedzenie > 0:
            postac.jedzenie -= 1
        else:
            postac.hp -= 3
            if postac.hp < 0:
                postac.hp = 0

        if postac.hp <= 0:
            print(f"[Alert]: {postac.imie} umarł z wycieńczenia na trasie!")
            break

        if random.random() < 0.05:
            print(f"[System]: Droga przerwana przez wydarzenie na {int(procent_drogi * 100)}% planowanej trasy.\n")
            event(postac)
            przerwano_marsz = True
            break

    if not przerwano_marsz and postac.hp > 0:
        if random.random() < 0.25:
            znalezisko = random.randint(5, 20)
            postac.punkty += znalezisko
            print(f"{postac.imie} znalazł na szlaku {znalezisko} kapsli!")

def powrot_do_krypty(postac: Postac, krypta: Krypta):
    print(f"=" * 60)
    print(f"[POWRÓT]: {postac.imie} rozpoczyna odwrót w stronę Krypty!")
    print(f"Pozycja startowa odwrotu: ({round(postac.x, 1)}, {round(postac.y, 1)})")
    print(f"Cel -> Krypta: ({krypta.x}, {krypta.y})")
    print(f"=" * 60)

    start_x = postac.x
    start_y = postac.y
    cel_x = krypta.x
    cel_y = krypta.y

    dystans_do_krypty = math.sqrt((cel_x - start_x)**2 + (cel_y - start_y)**2)
    
    jednostki_na_krok = 5 
    ilosc_krokow = max(1, int(dystans_do_krypty / jednostki_na_krok))

    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()

    pokazano_25 = False
    pokazano_50 = False
    pokazano_75 = False

    for i in range(1, ilosc_krokow + 1):
        procent_drogi = i / ilosc_krokow
        nowe_x = start_x + (cel_x - start_x) * procent_drogi
        nowe_y = start_y + (cel_y - start_y) * procent_drogi

        if postac.jedzenie > 0:
            turtle.pencolor("#00aaff") 
        else:
            turtle.pencolor("#ff0000") 
        
        turtle.goto(nowe_x, nowe_y)

        postac.x = nowe_x
        postac.y = nowe_y

        if postac.jedzenie > 0:
            postac.jedzenie -= 3
        else:
            postac.hp -= 6
            if postac.hp < 0:
                postac.hp = 0

        if postac.hp <= 0:
            print(f"\n[Alert]: {postac.imie} umarł z wycieńczenia w drodze powrotnej!")
            break

        if procent_drogi >= 0.25 and not pokazano_25:
            print(f"[Status]: Pokonano 25% drogi do bazy. Pozycja: ({round(postac.x, 1)}, {round(postac.y, 1)})")
            pokazano_25 = True
        elif procent_drogi >= 0.50 and not pokazano_50:
            print(f"[Status]: Pokonano 50% drogi do bazy. Pozycja: ({round(postac.x, 1)}, {round(postac.y, 1)})")
            pokazano_50 = True
        elif procent_drogi >= 0.75 and not pokazano_75:
            print(f"[Status]: Pokonano 75% drogi do bazy. Pozycja: ({round(postac.x, 1)}, {round(postac.y, 1)})")
            pokazano_75 = True
        elif i == ilosc_krokow:
            print(f"[Status]: Pokonano 100% drogi do bazy. Pozycja: ({round(postac.x, 1)}, {round(postac.y, 1)})")

#raport bo w wymaganiach bylo 
def generuj_raport(postac: Postac, start_jedzenie: int, rozmiar_mapy: int, kroki: int, przyczyna: str):
    print("\n" + "=" * 60)
    print("                      RAPORT KOŃCOWY WYPRAWY                      ")
    print("=" * 60)
    print(f" Imię zwiadowcy:       {postac.imie}")
    print(f" Parametry startowe:   Jedzenie: {start_jedzenie} | Rozmiar świata: {rozmiar_mapy}")
    print(f" Liczba wykonanych tur: {kroki}")
    print(f" Końcowa pozycja:      X: {round(postac.x, 1)}, Y: {round(postac.y, 1)}")
    print(f" Pozostałe zasoby:     HP: {postac.hp}/100 | Jedzenie: {postac.jedzenie}")
    print(f" Przyczyna zakończenia: {przyczyna}")
    print("-" * 60)
    
    if postac.hp <= 0:
        wynik_tekst = "PORAŻKA (Zwiadowca zginął na pustkowiach)"
    elif postac.punkty >= 100:
        wynik_tekst = "SUKCES (Powrót do Krypty w bogactwie!)"
    elif postac.punkty >= 40:
        wynik_tekst = "CZĘŚCIOWY SUKCES (Zwiadowca przetrwał i przyniósł zapasy)"
    else:
        wynik_tekst = "MINIMALNY SUKCES (Mało kapsli, ale skóra uratowana)"

    print(f" KOŃCOWY WYNIK:        {wynik_tekst}")
    print(f" ZDOBYTE KAPSLI:       {postac.punkty}")
    print("=" * 60 + "\n")