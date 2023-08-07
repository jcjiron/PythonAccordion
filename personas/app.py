from flask import Flask, render_template
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from database import db
from models import Persona

app = Flask(__name__)

# Configuración de nuestra base de datos:
USER_DB = 'postgres'
PASS_DB = 'postgres'
URL_DB = 'localhost'
NAME_DB = 'personas_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Flask migrate

migrate = Migrate()
migrate.init_app(app, db)

@app.route('/home')
def home():
    personas = Persona.query.all()
    count = Persona.query.count()
    app.logger.debug(f'Cantidad de personas: {count}')
    app.logger.debug(f'Personas: {personas}')
    return render_template('home.html', personas=personas, count=count)


class PersonasForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])


@app.route('/details/<int:id>')
def details(id):
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Details: {persona.id}')
    return render_template('details.html', persona=persona)

if __name__ == '__main__':
    app.run()
