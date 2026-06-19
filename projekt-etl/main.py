import pandas as pd
import sqlite3
import os

print("--- ROZPOCZĘCIE PROCESU ETL ---")

# ==========================================
# KROK 1: EXTRACT (POBIERANIE DANYCH)
# ==========================================
print("[1/3] Wczytywanie surowych danych z plików...")

if not os.path.exists("data/dostawy.csv") or not os.path.exists("data/cennik.json"):
    print("BŁĄD: Brak plików w folderze 'data'. Sprawdź ścieżki!")
    exit()

df_dostawy = pd.read_csv("data/dostawy.csv")
df_cennik = pd.read_json("data/cennik.json")


# ==========================================
# KROK 2: TRANSFORM (CZYSZCZENIE I LOGIKA)
# ==========================================
print("[2/3] Transformacja i czyszczenie syfu magazynowego...")

df_dostawy['quantity'] = pd.to_numeric(df_dostawy['quantity'], errors='coerce')

df_dostawy = df_dostawy.dropna(subset=['quantity'])

df_dostawy['quantity'] = df_dostawy['quantity'].clip(lower=0)

df_dostawy_pogrupowane = df_dostawy.groupby('product_id')['quantity'].sum().reset_index()

df_finalny_raport = pd.merge(df_dostawy_pogrupowane, df_cennik, on="product_id")

df_finalny_raport['total_value'] = df_finalny_raport['quantity'] * df_finalny_raport['price']


# ==========================================
# KROK 3: LOAD (ZAPIS DO BAZY SQL)
# ==========================================
print("[3/3] Tworzenie bazy danych SQLite i zapisywanie wyników...")

conn = sqlite3.connect('magazyn.db')


df_finalny_raport.to_sql('raport_finansowy', conn, if_exists='replace', index=False)


conn.close()

print("\n--- PROCES ZAKOŃCZONY SUKCESEM ---")
print("Podgląd wygenerowanego raportu finansowego:")
print(df_finalny_raport[['name', 'quantity', 'total_value']])