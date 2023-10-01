#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    if animal:
        return f'<h2>Animal ID {animal.id}</h2><ul><li>Name: {animal.name}</li><li>Species: {animal.species}</li><li>Zookeeper: {animal.zookeeper.name}</li><li>Enclosure: {animal.enclosure.environment}</li></ul>'
    else:
        return 'Animal not found'

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    if zookeeper:
        animals = ', '.join([animal.name for animal in zookeeper.animals])
        return f'<h2>Zookeeper {zookeeper.name}</h2><ul><li>Birthday: {zookeeper.birthday}</li><li>Animals: {animals}</li></ul>'
    else:
        return 'Zookeeper not found'

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    if enclosure:
        animals = ', '.join([animal.name for animal in enclosure.animals])
        return f'<h2>Enclosure</h2><ul><li>Environment: {enclosure.environment}</li><li>Open to Visitors: {enclosure.open_to_visitors}</li><li>Animals: {animals}</li></ul>'
    else:
        return 'Enclosure not found'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
