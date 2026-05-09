# ✦ Slavic Mythology: Digital Grimoire & Arena ✦

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org)
[![Framework](https://img.shields.io/badge/framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/database-SQLite3-003b57.svg)](https://sqlite.org)

Interaktivna veb aplikacija posvećena očuvanju i istraživanju slovenske mitologije. Projekat kombinuje digitalnu arhivu (Grimoar) sa sistemom za borbu (Arena), uz namenski razvijen administratorski panel za upravljanje podacima.

---

## 📖 Pregled Modula

### 1. Digitalni Grimoar (Frontend)
Vizueno bogat interfejs koji simulira autentičnu drevnu knjigu. 
- **Responzivni UX:** Inteligentno upravljanje prostorom na mobilnim uređajima; lista bića se transformiše u navigacioni meni koji oslobađa punu širinu ekrana za čitanje.
- **Dizajnerski detalji:** Napredna manipulacija CSS filterima (`sepia`, `contrast`, `blend-mode`) i dinamički generisani kaligrafski inicijali.

### 2. Admin Panel (Desktop)
Lokalna Python aplikacija bazirana na `tkinter` biblioteci.
- Omogućava CRUD operacije nad bazom podataka bez potrebe za SQL znanjem.
- Direktno mapiranje statistika za Arenu (HP, Attack, Defense).

### 3. Arena (Backend)
Sistem zasnovan na Flask framework-u koji dinamički povlači statistike iz SQLite baze, pripremajući teren za logiku borbe.

---

## 🛠 Tehnološki Stack

| Komponenta | Tehnologija |
| :--- | :--- |
| **Backend** | Python / Flask |
| **Baza podataka** | SQLite3 |
| **GUI (Admin)** | Tkinter |
| **Frontend** | HTML5, CSS3 (Modern Flexbox), Vanilla JS |
| **Deployment** | Git / Render.com |

---

## ⚙️ Instalacija i Konfiguracija

### Lokalno pokretanje
1. Klonirajte repozitorijum:
   ```bash
   git clone [https://github.com/vas-username/slavenska-mitologija.git](https://github.com/vas-username/slavenska-mitologija.git)

    Instalirajte neophodne biblioteke:
    Bash

pip install flask

Pokrenite server:
Bash

    python app.py

Upravljanje podacima

Za dodavanje novih bića, pokrenite administratorski alat:
Bash

python admin_panel.py

🔄 Kontinuirana Integracija (CI/CD)

Projekat koristi Git-based deployment model. S obzirom na to da je baza podataka SQLite (fajl sistem), proces ažuriranja je sledeći:

    Lokalna izmena: Unos podataka putem Admin Panela.

    Commit: git add mitologija.db && git commit -m "Update: New creature data"

    Push: git push origin main

    Deploy: Render.com automatski detektuje promenu, povlači novu verziju baze i restartuje instancu aplikacije.

📐 Arhitektura Podataka (Schema)

Tabela bica u SQLite bazi sadrži sledeće atribute:

    ime (TEXT) - Primarni ključ / Naziv bića.

    opis (TEXT) - Detaljna legenda/priča.

    slika (TEXT) - Putanja do fajla u static/slike/.

    hp, snaga, oklop (INTEGER) - Statistike za borbeni sistem.

🛡 Licenca

Ovaj projekat je razvijen u edukativne svrhe i otvoren je za doprinose zajednice.

Autor: [VLADE 2026]

Kontakt:(https://github.com/grujo85)
