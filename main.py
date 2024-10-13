import string
from collections import defaultdict

def przeksztalc_tekst(wpis):
    konwerter = str.maketrans('', '', string.punctuation)
    return wpis.translate(konwerter).lower().split()

ilosc_plikow = int(input("Podaj liczbę plików: "))

zbior_plikow = []

for numer in range(ilosc_plikow):
    tresc_pliku = input(f"Wprowadź treść pliku {numer}: ").strip()
    zbior_plikow.append(tresc_pliku)

ilosc_pytan = int(input("Podaj liczbę zapytań: "))

zbior_pytan = []

for numer_pytania in range(ilosc_pytan):  # Poprawione "in range"
    zapytanie = input(f"Wprowadź zapytanie {numer_pytania}: ").strip().lower()
    zbior_pytan.append(zapytanie)

mapa_wynikow = defaultdict(lambda: defaultdict(int))

for indeks_pliku, plik in enumerate(zbior_plikow):
    zmodyfikowany_plik = przeksztalc_tekst(plik)

    for pytanie in zbior_pytan:
        liczba_wystapien = zmodyfikowany_plik.count(pytanie)
        mapa_wynikow[indeks_pliku][pytanie] = liczba_wystapien

for pytanie in zbior_pytan:
    lista_wystapien = [(indeks_pliku, mapa_wynikow[indeks_pliku][pytanie]) for indeks_pliku in range(ilosc_plikow) if
                       mapa_wynikow[indeks_pliku][pytanie] > 0]

    lista_wystapien.sort(key=lambda x: (-x[1], x[0]))

    wynik_koncowy = [indeks_pliku for indeks_pliku, _ in lista_wystapien]
    print(wynik_koncowy)

