from flask import *
import sqlite3
from random import *
 
# Création d'un objet application web Flask
app = Flask(__name__, static_url_path='/static')

# Fonctions utilisées pour appeler des commandes SQL
def lire_base():
    """ Récupere les cartes dans la table pour la lire
        Renvoie (list of tuples) : liste des cartes
    """
    connexion = sqlite3.connect("BDD/BD.clash_royale.db")
    curseur = connexion.cursor()
    requete_sql = """
    SELECT *
    FROM Clash_royale"""
    resultat = curseur.execute(requete_sql)
    cartes = resultat.fetchall() 
    # On recupere les cartes et on les mets sous forme de tuple
    connexion.close()
    return cartes


# Création d'une fonction accueillir() associee a l'URL "/"
# pour générer une page web dynamique
@app.route("/")
def accueill():
    """Présentation du site"""
    return render_template("accueillir.html")

# Page utilisant une base de données
@app.route("/deck")
def deck_choisie():
    # Récupération des personnes de la base de données SQLite
    cr = lire_base()
    connexion = sqlite3.connect("BDD/BD.clash_royale.db")
    curseur = connexion.cursor()
    requete_sql = """
    SELECT lien_img 
    FROM Clash_royale
    ORDER BY Random()
    LIMIT 8"""
    deck = curseur.execute(requete_sql)
    connexion.close()
    # Transmission pour affichage
    return render_template("gen.html",cartes=deck)

# Lancement de l'application web et son serveur
# accessible à l'URL : http://127.0.0.1:1664/
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, debug=True)