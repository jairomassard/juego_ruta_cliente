import json
import googlemaps
import os

# Tu clave API de Google Maps
API_KEY = 'AIzaSyCs9CH_C9oCmhQpJksJMlKa4vE1BpbuiIM'

# Inicializa el cliente de Google Maps
gmaps = googlemaps.Client(key=API_KEY)

# Coordenadas de los puntos de inicio y el taller
start_points = [
    {"lat": 4.675012904403253, "lng": -74.06580527473798},  # Punto 1
    {"lat": 4.672103505674668, "lng": -74.06313815035868},  # Punto 2
    {"lat": 4.669537136414592, "lng": -74.07157101457376},  # Punto 3
    {"lat": 4.675257988352596, "lng": -74.05954399067413}   # Punto 4
]

workshop_location = {"lat": 4.670607316343895, "lng": -74.06642754716098}  # Taller

# Almacena las rutas generadas
routes = {}

# Función para generar la ruta entre dos puntos
def generate_route(start_point, workshop_location):
    result = gmaps.directions(
        origin=(start_point["lat"], start_point["lng"]),
        destination=(workshop_location["lat"], workshop_location["lng"]),
        mode="driving"
    )
    return result

# Generar las rutas y guardarlas
for idx, start_point in enumerate(start_points):
    route = generate_route(start_point, workshop_location)
    routes[f'route_{idx + 1}'] = route

# Ruta para guardar el archivo routes.json
output_dir = '../routes'  # Ajusta la ruta para guardar el archivo en la carpeta /routes
if not os.path.exists(output_dir):
    os.makedirs(output_dir)  # Crea la carpeta si no existe

# Guardar las rutas en un archivo JSON
with open(os.path.join(output_dir, 'routes.json'), 'w') as f:
    json.dump(routes, f, indent=4)

print("Rutas generadas y guardadas en /routes/routes.json.")


# Para ejecutar este script debe primero ubicarse dentro del entorno virtual en la carpeta scripts
# cd scripts  
# python generate_routes.py
# luego para volver al directorio raiz del programa poner:
# cd C:\Prog_juego_ubicacion_taller
