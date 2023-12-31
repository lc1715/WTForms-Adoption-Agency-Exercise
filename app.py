from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, Pet
from forms import PetForm
from sqlalchemy.sql import text

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "oh-so-secret"

connect_db(app)


@app.route('/')
def show_all_pets():
    """Show all pets"""

    pets = Pet.query.all()
    return render_template('show_all_pets.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def show_add_pet_form():
    """Show the add pet form if receive a GET request or add a new pet to the db if 
    receive a POST request, CSRF token is present, and validators are validated """

    form = PetForm()
    if form.validate_on_submit():
        pet_name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data or None 
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(pet_name=pet_name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()

        flash(f'{pet_name} has been added to the pet list!')
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)
   
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_edit_pet_form(pet_id):
    """Show the edit pet form if the route receives a GET request or edit a new pet 
    to the db if route receive a POST request, CSRF token is present, and validators 
    are validated"""

    change_pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=change_pet)

    if form.validate_on_submit():

        change_pet.pet_name = form.pet_name.data
        change_pet.photo_url = form.photo_url.data or None
        change_pet.notes = form.notes.data
        change_pet.available = form.available.data

        db.session.commit()  

        flash(f'Edited pet: {change_pet.pet_name}')  
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', form=form, change_pet=change_pet)
