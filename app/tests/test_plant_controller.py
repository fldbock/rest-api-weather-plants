from app.models.plant import Plant
from app.controllers.plant_controller import PlantController

class TestPlantController:
    # Create
    def test_create_app(self, app):
        with app.app_context():            
            plant_controller = PlantController()    
            plant_controller.create("Plant 3", 70.70, 80.80)

            plants = plant_controller.read()

            assert len(plants) == 3
            assert plants[2]["name"] == "Plant 3" and plants[2]["lat"] == 70.70 and plants[2]["long"] == 80.80
    
    def test_create_plant_name_none(self, app):
        with app.app_context():            
            plant_controller = PlantController()    
            response = plant_controller.create(None, 70.70, 80.80)

            plants = plant_controller.read()

            assert len(plants) == 2
            assert response[0]["error"] == "You should supply a valid name, lat and long" and response[1] == 404

    # Read
    def test_read(self, app):
        with app.app_context():            
            plant_controller = PlantController()            
            plants = plant_controller.read()
            assert len(plants) == 2
            assert plants[0]["name"] == "Plant 1" and plants[1]["name"] == "Plant 2"


    # Update
    def test_update_plant_that_exists(self, app):
        with app.app_context():            
            plant_controller = PlantController()    
            plant_controller.update(1, "Plant 3", 70.70, 80.80)

            plants = plant_controller.read()

            assert len(plants) == 2
            assert plants[0]["name"] == "Plant 3" and plants[0]["lat"] == 70.70 and plants[0]["long"] == 80.80
    
    def test_update_plant_name_none(self, app):
        with app.app_context():            
            plant_controller = PlantController()    
            response = plant_controller.update(1, None, 70.70, 80.80)

            plants = plant_controller.read()

            assert len(plants) == 2
            assert response[0]["error"] == "You should supply a valid name, lat and long" and response[1] == 404

    def test_update_plant_that_does_not_exist(self, app):
        with app.app_context():            
            plant_controller = PlantController()    
            response = plant_controller.update(3, "Plant 3", 70.70, 80.80)

            plants = plant_controller.read()

            assert len(plants) == 2
            assert response[0]["error"] == "Plant not found" and response[1] == 404

    # Delete
    def test_delete_plant_that_exists(self, app):
        with app.app_context():            
            plant_controller = PlantController()    
            plant_controller.delete(1)

            plants = plant_controller.read()

            assert len(plants) == 1
            assert plants[0]["name"] == "Plant 2" and plants[0]["lat"] == 60.60 and plants[0]["long"] == 60.60

    def test_delete_plant_that_does_not_exist(self, app):
        with app.app_context():            
            plant_controller = PlantController()    
            response = plant_controller.delete(3)

            plants = plant_controller.read()

            assert len(plants) == 2
            assert response[0]["error"] == "Plant not found" and response[1] == 404
