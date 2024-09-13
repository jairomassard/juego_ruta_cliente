import os
from flask import Flask, send_from_directory, render_template, make_response
import geopy
from geopy.geocoders import GoogleV3
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()

app = Flask(__name__)

# sin railway
#@app.route('/')
#def index():
#    return render_template('index.html')

@app.route('/')
def index():
    api_key = os.getenv('GOOGLE_API_KEY')
    return render_template('index.html', api_key=api_key)

@app.route('/static/<path:filename>')
def serve_static(filename):
    response = make_response(send_from_directory('static', filename))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory('.', 'manifest.json')

@app.route('/service-worker.js')
def serve_service_worker():
    return send_from_directory('.', 'service-worker.js')

@app.route('/icons/<path:filename>')
def serve_icons(filename):
    return send_from_directory('icons', filename)

# Ruta para servir el archivo routes.json desde la carpeta /routes
@app.route('/routes/routes.json')
def serve_routes():
    return send_from_directory('routes', 'routes.json')

# Ruta para servir el archivo preguntas.json desde la carpeta /preguntas
@app.route('/preguntas/preguntas.json')
def serve_questions():
    return send_from_directory('preguntas', 'preguntas.json')

if __name__ == '__main__':
    # Especifica las rutas del certificado y la clave generados por mkcert
    app.run(ssl_context=('localhost.pem', 'localhost-key.pem'), debug=True)


