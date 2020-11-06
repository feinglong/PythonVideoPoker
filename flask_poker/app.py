from flask import Flask, render_template, redirect, request, escape, session
import random
from fonctions import premier_tirage, deuxieme_tirage, gain

app = Flask(__name__)
app.secret_key = "Casino_Royale"

# HAND_NB = 5
POST = 'POST'
GET = 'GET'
deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']



@app.route('/')
def home():
    return render_template(
        'index.html', 
        bankroll = session['bankroll'] if 'bankroll' in session else None,
        error = session['error'] if 'error' in session else None,
        )


@app.route('/reset', methods=[GET])
def reset():
    session.clear()
    return redirect("/", code=302)

@app.route('/premier-tirage', methods=[GET])
@app.route('/second-tirage', methods=[GET])
def go_home():
    return redirect("/", code=302)



@app.route('/premier-tirage', methods=[POST])
def firstDraw():
    # banroll check
    bankroll = int(escape(request.form['bankroll']))
    mise_joueur = int(escape(request.form['mise_joueur']))
    if not bankroll or not mise_joueur or bankroll < 0 or mise_joueur < 0:
        session['error'] = "Bankroll or Bet not found... Please try again."
        return redirect('/', code=302)
    if bankroll - mise_joueur < 0 :
        session['error'] = "Not enough money... Please insert more money."
        return redirect('/',code =302)
    session["error"] = ""
    session['bankroll'] = bankroll - mise_joueur
    session['mise_joueur'] = mise_joueur
    # premier_tirage(deck):
    pt_jeu, nv_deck  = premier_tirage(deck)
    session['deck'] = nv_deck
    return render_template(
        'premier-tirage.html', 
        pt_jeu = pt_jeu,
        bankroll = session['bankroll'],
        mise_joueur = session['mise_joueur'],
    )
    
@app.route('/second-tirage', methods=[POST])
def secondDraw():
    # Récupération de la main du premier tirage
    main = []
    for carte in request.form:
        main.append(escape(carte))
    # Second tirage
    dt_jeu = deuxieme_tirage(session['deck'], main)
    g, resultat = gain(dt_jeu, session['mise_joueur'])
    session['bankroll'] = session['bankroll'] + g 
    
    return render_template(
        'second-tirage.html',
        bankroll = session['bankroll'],
        mise_joueur = session['mise_joueur'],
        dt_jeu = dt_jeu,
        resultat = resultat   
    )

if __name__ == "__main__":
    app.run(debug=True)
    