from app.models.plant import Plant
import requests
from flask import jsonify

class WeatherController:

    def read(self, id, datetime):
        plant = Plant.query.session.get(Plant, id)

        if plant is None:
            return {'error': 'Plant not found'}, 404
        
        # Construct endpoint
        lat = plant.lat
        long = plant.long

        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m,relative_humidity_2m"
        
        # Make API Call
        try:
            response = requests.get(url)

            json_data = response.json()
            json_data = json_data['hourly']
            index = json_data['time'].index(datetime)

            return {'temperature': json_data['temperature_2m'][index], 'humidity': json_data['relative_humidity_2m'][index]}, 200
        except Exception as e:
            return {'error': 'External API does not have data for this datetime'}, 500
