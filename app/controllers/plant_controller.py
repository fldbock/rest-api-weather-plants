from app.models.plant import Plant

class PlantController:

    def read(self):
        plants = Plant.query.all()
        serialized_plants = [plant.serialize() for plant in plants]

        return serialized_plants

    def create(self, name, lat, long):          
        plant = Plant(name=name, lat=lat, long=long)
        
        return self.save_or_404(plant)         
        
    def update(self, id, name, lat, long):            
        plant = Plant.get(id)

        if plant is None:
            return {'error': 'Plant not found'}, 404
        
        plant.name = name
        plant.lat = lat
        plant.long = long
        
        return self.save_or_404(plant)
    
    def delete(self, id):
        plant = Plant.get(id)
        
        if plant is None:
            return {'error': 'Plant not found'}, 404
        
        plant.destroy()

        return {'message': 'Plant deleted successfully'}, 200
    
    def save_or_404(self, plant):
        if not plant.save():
            return {'error': 'You should supply a valid name, lat and long'}, 404

        return plant.serialize(), 200


