# ✦ Slavic Mythology: Digital Grimoire & Arena ✦

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org)
[![Framework](https://img.shields.io/badge/framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/database-SQLite3-003b57.svg)](https://sqlite.org)

An interactive web application dedicated to the preservation and exploration of Slavic mythology. This project combines a digital archive (The Grimoire) with a combat system (The Arena), featuring a custom-built administrative panel for data management.

---

## 📖 Module Overview

### 1. Digital Grimoire (Frontend)
A visually rich interface designed to simulate an authentic ancient manuscript.
- **Responsive UX:** Intelligent screen real-estate management for mobile devices; the creature list transforms into a navigation menu, freeing up full-width space for an immersive reading experience.
- **Design Elements:** Advanced CSS filter manipulation (`sepia`, `contrast`, `blend-mode`) and dynamically generated calligraphic initials.

### 2. Admin Panel (Desktop)
A local Python application built with the `tkinter` library.
- Enables full CRUD operations on the database without requiring SQL knowledge.
- Direct mapping of combat statistics for the Arena (HP, Attack, Defense).

### 3. Arena (Backend)
A Flask-based system that dynamically pulls stats from the SQLite database, laying the groundwork for turn-based combat logic.

---

## 🛠 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend** | Python / Flask |
| **Database** | SQLite3 |
| **GUI (Admin)** | Tkinter |
| **Frontend** | HTML5, CSS3 (Modern Flexbox), Vanilla JS |
| **Deployment** | Git / Render.com |

---

## ⚙️ Installation & Configuration

### Local Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/grujo85/slavic-mythology.git](https://github.com/grujo85/slavic-mythology.git)

    Install the required dependencies:
    Bash

   pip install flask

Run the server:
Bash

    python app.py

Data Management

To add or update mythical creatures, run the administrative tool:
Bash

python admin_panel.py

🔄 Continuous Integration (CI/CD)

The project follows a Git-based deployment model. Since the database is a file-based SQLite system, the update workflow is as follows:

    Local Update: Input data via the Admin Panel on your local machine.

    Commit: git add mitologija.db && git commit -m "Update: New creature data added"

    Push: git push origin main

    Deploy: Render.com automatically detects the push, pulls the updated database, and redeploys the application instance.

📐 Data Schema

The bica table in the SQLite database consists of the following attributes:

    ime (TEXT) - Primary Key / Name of the creature.

    opis (TEXT) - Detailed lore and legends.

    slika (TEXT) - Filename path located in static/slike/.

    hp, snaga, oklop (INTEGER) - Combat statistics (Health, Attack, Defense).

🛡 Licenca

Ovaj projekat je razvijen u edukativne svrhe i otvoren je za doprinose zajednice.

Autor: [VLADE 2026]

Kontakt:(https://github.com/grujo85)
