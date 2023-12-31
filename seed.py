"""Seed file to make sample data for db."""

from models import Pet, db
from app import app


# Create all tables
db.drop_all()
db.create_all()

# Delete all of the pets in the pets table
Pet.query.delete()

# Add sample pets
scruffy = Pet(pet_name='Scruffy', species='dog', photo_url='https://images.unsplash.com/photo-1537151608828-ea2b11777ee8?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjJ8fGRvZ3N8ZW58MHx8MHx8fDA%3D', age=1, available=True)
woofly = Pet(pet_name='Woofly', species='dog', photo_url='https://images.unsplash.com/photo-1568572933382-74d440642117?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8ZG9nc3xlbnwwfHwwfHx8MA%3D%3D', age=2, available=True)
scout= Pet(pet_name='Scout', species='cat', photo_url='https://images.unsplash.com/photo-1593483316242-efb5420596ca?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTYzfHxjYXR8ZW58MHx8MHx8fDA%3D', age=2, available=True)
porchetta = Pet(pet_name='Porchetta', species='porcupine', photo_url='http://kids.sandiegozoo.org/sites/default/files/2017-12/porcupine-incisors.jpg', age=4, notes='Somewhat spikey', available=True)
oreo = Pet(pet_name='Oreo', species='dog', age=4, available=False)



db.session.add_all([scruffy, woofly, scout, porchetta, oreo])

db.session.commit()