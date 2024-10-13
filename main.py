import string
from collections import defaultdict


def wyczysc_tekst(tekst):
    translator = str.maketrans('', '', string.punctuation)
    return tekst.translate(translator).lower().split()

liczba_dokumentow = int(input("Ile dokumentów chcesz wprowadzić? "))

dokumenty = []

for i in range(1, liczba_dokumentow + 1):
    dokument = input(f"Wpisz treść dokumentu {i}: ").strip()
    dokumenty.append(dokument)

liczba_slow = int(input("Ile zapytań chcesz wprowadzić? "))


slowa = []

for i in range(1, liczba_slow + 1):
    slowo = input(f"Wpisz zapytanie {i}: ").strip().lower()  # Zamiana na małe litery
    slowa.append(slowo)

wyniki = defaultdict(lambda: defaultdict(int))

for i, dokument in enumerate(dokumenty):
    dokument_id = i  # Indeks dokumentu

    oczyszczony_dokument = wyczysc_tekst(dokument)

    for slowo in slowa:
        liczba_wystapien = oczyszczony_dokument.count(slowo)  # Zliczanie słowa w oczyszczonym dokumencie
        wyniki[dokument_id][slowo] = liczba_wystapien

for slowo in slowa:
    dokumenty_wyniki = [(doc_id, wyniki[doc_id][slowo]) for doc_id in range(liczba_dokumentow) if
                        wyniki[doc_id][slowo] > 0]

    dokumenty_wyniki.sort(key=lambda x: (-x[1], x[0]))

    wynik = [doc_id for doc_id, _ in dokumenty_wyniki]
    print(wynik)

