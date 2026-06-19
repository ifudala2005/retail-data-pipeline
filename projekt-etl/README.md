# Retail Data Pipeline (ETL) 🛒

## Opis Projektu
Automatyczny skrypt ETL (Extract, Transform, Load) napisany w Pythonie, zaprojektowany do integracji rozproszonych danych sklepowych. Projekt rozwiązuje realny problem biznesowy: łączenie surowych, często błędnych danych z dostaw (pliki płaskie) z zewnętrznymi cennikami.

## Technologie
* **Python 3**
* **Pandas** (Data manipulacja i czyszczenie)
* **SQLite** (Baza danych)

## Funkcjonalności
* **Extract:** Wczytywanie asortymentu z plików CSV (dostawy magazynowe) oraz API (symulacja pliku JSON z cennikami).
* **Transform:** Czyszczenie danych transakcyjnych (usuwanie wartości NULL, korekta ujemnych stanów magazynowych do zera, agregacja ilości sztuk w przypadku zdublowanych dostaw).
* **Load:** Obliczanie całkowitej wartości zatowarowania i zrzut czystego raportu.