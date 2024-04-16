from app.models.plant import Plant

class PlantController:

    def index(self):
        plants = Plant.query.all()
        serialized_plants = [plant.serialize() for plant in plants]

        return serialized_plants

    def create(self, name, lat, long):
        if name is None or lat is None or long is None:
            return {'error': 'You should supply a valid name, lat and long'}, 404
        plant = Plant(name=name, lat=lat, long=long)
        plant.save()
        
        return plant.serialize(), 201
    def update(self, id, name, lat, long):
        if name is None or lat is None or long is None:
            return {'error': 'You should supply a valid name, lat and long'}, 404
        plant = Plant.get(id)

        if plant is None:
            return {'error': 'Plant not found'}, 404
        
        plant.name = name
        plant.lat = lat
        plant.long = long
        
        plant.save()

        return plant.serialize(), 200
    def remove(self, id):
        plant = Plant.get(id)
        
        if plant is None:
            return {'error': 'Plant not found'}, 404
        
        plant.destroy()

        return {'message': 'Plant deleted successfully'}, 200


