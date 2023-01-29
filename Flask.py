from flask import Flask, render_template
app = Flask(__name__)
@app.route('/') # decorator
@app.route('/home')
def home_page():
    return render_template('home.html')
@app.route('/cars')
def cars_page():
    item= ['FORD', 'FERRARI','TOYOTA','LAMBORGINI','LANCIA']
    return render_template('cars.html',items = item)
@app.route('/breakdown')
def analytics():
    return render_template('breakdown.html')