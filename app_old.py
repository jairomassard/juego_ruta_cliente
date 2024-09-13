from flask import Flask, send_from_directory, render_template
import geopy
from geopy.geocoders import GoogleV3

app = Flask(__name__)

# Instancia del geolocalizador usando tu API Key
geolocator = GoogleV3(api_key='AIzaSyCs9CH_C9oCmhQpJksJMlKa4vE1BpbuiIM')

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para servir el archivo routes.json desde la carpeta /routes
@app.route('/routes/routes.json')
def serve_routes():
    return send_from_directory('routes', 'routes.json')

# Ruta para servir el archivo preguntas.json desde la carpeta /preguntas
@app.route('/preguntas/preguntas.json')
def serve_questions():
    return send_from_directory('preguntas', 'preguntas.json')

if __name__ == '__main__':
    app.run(debug=True)

