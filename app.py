from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blackjack')
def blackjack():
    return render_template("blackjack.html")

@app.route('/russian_roulette')
def russian_roulette():
    return render_template("russian_roulette.html")

@app.route('/plinko')

def plinko():
    return render_template("plinko.html")

if __name__ == '__main__':
    app.run(debug=True)