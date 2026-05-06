import sqlite3
import re

def dodaj_bice():
    # Povezivanje sa postojećom bazom
    conn = sqlite3.connect('mitologija.db')
    cursor = conn.cursor()

    print("--- 📝 GENERATOR MITOLOŠKIH BIĆA ---")
    print("Unesite tekst o biću (Prva reč mora biti ime).")
    print("Kucajte 'kraj' za završetak.\n")

    while True:
        tekst = input("Nalepi tekst ovde: ").strip()
        
        if tekst.lower() == 'kraj':
            break
        
        if not tekst:
            continue

        # 1. Automatsko izvlačenje imena (prva reč pre zareza ili razmaka)
        match = re.match(r"^([\w\-]+)", tekst)
        if match:
            ime = match.group(1)
        else:
            print("❌ Greška: Ne mogu da prepoznam ime na početku rečenice.")
            continue

        # 2. Generisanje imena slike (npr. "Anđama" -> "andjama.jpg")
        slika_ime = f"{ime.lower().replace('č', 'c').replace('ć', 'c').replace('ž', 'z').replace('š', 's')}.jpg"

        # 3. Unos dodatnih informacija
        print(f"\nPrepoznato ime: **{ime}**")
        kategorija = input(f"Unesi kategoriju za {ime} (npr. Šumski duhovi): ")
        try:
            opasnost = int(input(f"Unesi nivo opasnosti (0-10) za {ime}: "))
        except ValueError:
            opasnost = 5  # Podrazumevana vrednost ako pogrešiš

        # 4. Upis u bazu
        try:
            cursor.execute('''
                INSERT INTO bica (ime, opis, slika, kategorija, opasnost)
                VALUES (?, ?, ?, ?, ?)
            ''', (ime, tekst, slika_ime, kategorija, opasnost))
            
            conn.commit()
            print(f"✅ Uspešno dodato u bazu: {ime}\n" + "-"*30)
        except Exception as e:
            print(f"❌ Greška pri upisu u bazu: {e}")

    conn.close()
    print("\nRad završen. Baza je ažurirana!")

if __name__ == "__main__":
    dodaj_bice()
