from flask import render_template
from app import app
from app.models.adoption_list import adoptions

@app.route('/')
def index():
    return render_template('index.html', title='Home', adoptions=adoptions)


@app.route('/dog/<index>')
def see_adopted_dogs(index):
    chosen_adoption = adoptions[int(index)]
    return render_template('dog.html', title='Info', adoption=chosen_adoption)

