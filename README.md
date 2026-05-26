# Symulator Ekspedycji: Fallout

Projekt zaliczeniowy napisany w języku Python 3.11, kompatybilny ze standardową biblioteką (brak konieczności instalacji zewnętrznych pakietów).

## Struktura projektu
Projekt składa się z 3 plików źródłowych (łączny rozmiar < 15 kB):
* `main.py` – główny plik startowy i konfiguracja interfejsu
* `mechanika.py` – logika poruszania się, zdarzenia losowe oraz system raportowania
* `modele.py` – struktura obiektów (Postać, Mapa, Krypta)

## Wymagania systemowe
* Python 3.11 (lub nowszy)
* Środowisko graficzne obsługujące bibliotekę `turtle`
* [Zalecane] Visual Studio Code z zainstalowanym rozszerzeniem Python

## Instrukcja uruchomienia

1. Pobierz i wypakuj wszystkie trzy pliki (`main.py`, `mechanika.py`, `modele.py`) do jednego, wspólnego folderu.
2. Otwórz terminal (Konsolę/Wiersz poleceń) w tym folderze.
3. Uruchom program za pomocą polecenia:
  `python main.py`

## Instrukcja uruchomienia (Zalecana)

1. Pobierz i wypakuj pliki projektu (`main.py`, `mechanika.py`, `modele.py`) do jednego folderu.
2. Otwórz program **Visual Studio Code**.
3. W menu górnym wybierz `File` -> `Open Folder...` i wskaż folder z plikami gry.
4. Otwórz plik `main.py` w edytorze.
5. Uruchom program, klikając ikonę **Play** (Run Python File) w prawym górnym rogu VSC lub używając skrótu klawiszowego `F5`.
