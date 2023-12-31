from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

default_photo_url = 'https://www.creativefabrica.com/wp-content/uploads/2021/07/04/cat-and-dog-silhouette-logo-for-pet-shop-Graphics-14248406-1.jpg'

class Pet(db.Model):
    """The pet table called pets. It's also the model(class), Pet, and it has
    all of the attributes (key-value) pairs in it"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False, default=default_photo_url)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

