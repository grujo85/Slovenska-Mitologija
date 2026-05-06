from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def uzmi_iz_baze(upit=""):
    conn = sqlite3.connect('mitologija.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    if upit:
        # Sortiramo rezultate pretrage azbučno
        cursor.execute("SELECT * FROM bica WHERE ime LIKE ? ORDER BY ime", ('%' + upit + '%',))
    else:
        # Sortiramo sva bića azbučno
        cursor.execute("SELECT * FROM bica ORDER BY ime")
    rezultati = cursor.fetchall()
    conn.close()
    return rezultati

@app.route('/')
def galerija():
    pretraga = request.args.get('search', '')
    podaci = uzmi_iz_baze(pretraga)
    return render_template('galerija.html', bica=podaci)

if __name__ == '__main__':
    app.run(debug=True)
