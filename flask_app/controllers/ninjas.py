from pprint import pprint
from flask_app import app, render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


# display form to create a ninja
@app.get('/ninjas/new')
def new_ninja():
    dojos = Dojo.find_all()
    return render_template('new_ninja.html', dojos = dojos)


# process form and create a ninja
@app.post('/ninjas')
def create_ninja():
    ninja_id = Ninja.save(request.form)
    print(f'**** CREATED - NINJA ID: {ninja_id} ****')
    return redirect(f'/dojos/{request.form["dojo_id"]}')
