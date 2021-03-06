from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/evaluacion')
def evaluacion():
    return  render_template('evaluacion.html')

@app.route('/registro')
def registro():
    return  render_template('registro.html')
    
@app.route('/inicio')
def inicio():
    return  render_template('inicio.html')

if __name__ == '__main__':
    app.run(debug=True)
