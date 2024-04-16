from flask import request
from app.controllers.plant_controller import PlantController
from app.controllers.weather_controller import WeatherController

def register_routes(app, db):

    @app.route('/plants', methods=['GET'])
    def list_plants():
        return PlantController().index()

    @app.route('/plants', methods=['POST'])
    def create_plant():
        name = request.form.get('name')
        lat = request.form.get('lat')
        long = request.form.get('long')

        return PlantController().create(name, lat, long)

    @app.route('/plants/<int:plant_id>', methods=['PUT'])
    def update_plant(plant_id):
        name = request.form.get('name')
        lat = request.form.get('lat')
        long = request.form.get('long')
        return PlantController().update(plant_id, name, lat, long)

    @app.route('/plants/<int:plant_id>', methods=['DELETE'])
    def delete_plant(plant_id):
        return PlantController().remove(plant_id)
    
    @app.route('/plants/<int:plant_id>/weather', methods=['GET'])
    def get_plant_weather(plant_id):
        datetime = request.args.get("datetime")
        return WeatherController().show(plant_id, datetime)