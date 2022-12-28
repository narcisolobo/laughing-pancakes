from pprint import pprint
from flask_app import app, render_template, redirect, request
from flask_app.models.dojo import Dojo


# redirect the user to /dojos
@app.get('/')
def redirect_user():
    return redirect('/dojos')


# display all dojos
@app.get('/dojos')
def all_dojos():
    dojos = Dojo.find_all()
    print(f'**** FOUND - ALL DOJOS: ****')
    pprint(dojos)
    return render_template('dojos.html', dojos = dojos)


# display one dojo by id
@app.get('/dojos/<int:dojo_id>')
def one_dojo(dojo_id):
    print(f'{"*" * 20} IN THE ONE_DOJO FUNCTION {"*" * 20}')
    data = {
        'id': dojo_id
    }
    dojo = Dojo.find_by_id_with_ninjas(data)
    print(f'**** FOUND - DOJO: {dojo} ****')
    return render_template('one_dojo.html', dojo = dojo)


# process form and create a dojo
@app.post('/dojos')
def create_dojo():
    dojo_id = Dojo.save(request.form)
    print(f'**** CREATED - DOJO ID: {dojo_id} ****')
    return redirect('/dojos')
