from app.main import db

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column('Id', db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column('Name', db.String(), nullable=False)
    lat = db.Column('Lat', db.Float(), nullable=False)
    long = db.Column('Long', db.Float(), nullable=False)

    def __init__(self, name, lat, long):
        self.name = name
        self.lat = lat
        self.long = long
        db.session.add(self)

    @staticmethod
    def get(id):
        return Plant.query.session.get(Plant, id)

    def save(self):        
        db.session.commit()

    def destroy(self):
        db.session.delete(self)
        self.save()

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'lat': self.lat,
            'long': self.long,
        }
    def __repr__(self):
        return f'This is a plant named {self.name} with latitude {self.lat} and longitude {self.long}'
    