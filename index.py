from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

# Initialisation de Flask
app = Flask(__name__)

# Création de la connection à la bdd
def get_connection():
 return psycopg2.connect(
  host='localhost',
  database='flask_garage',
  user='garadm7841',
  password='SP7c3$@uwL84jmSEoP3',
  port=5432,
  cursor_factory=RealDictCursor
 )

# Route pour accéder à la 1e page
@app.route('/')
def index():
 return 'Voici mon super garage tautomobile !'

# Route pour accéder à toutes les voitures
@app.route('/cars', methods=['GET'])
def get_all_cars():
 connection = get_connection()
 cursor = connection.cursor()
 
 cursor.execute('SELECT * FROM car')
 cars = cursor.fetchall()

 cursor.close()
 connection.close()

 return jsonify(cars)

# Route pour accéder à une voiture par son id
@app.route('/cars/<int:id>', methods=['GET'])
def getCarById(id):
 connection = get_connection()
 cursor = connection.cursor()

 cursor.execute('SELECT * FROM car WHERE car_id = %s', (id,))
 oneCar = cursor.fetchone()

 cursor.close()
 connection.close()

 return jsonify(oneCar)

# Route pour accéder à toutes les voitures par leur marque
@app.route('/cars/brand/<string:brand>', methods=['GET'])
def getCarsByBrand(brand):
 connection = get_connection()
 cursor = connection.cursor()

 cursor.execute('SELECT * FROM car WHERE brand = %s', (brand,))
 carsByBrand = cursor.fetchmany(5)

 cursor.close()
 connection.close()

 return jsonify(carsByBrand)

# Route pour ajouter un modèle de voiture
@app.route('/cars', methods=['POST'])
def addOneCar():
 data = request.get_json()

 brand = data['brand']
 model = data['model']

 connection = get_connection()
 cursor = connection.cursor()

 cursor.execute('INSERT INTO car (brand, model) VALUES (%s, %s) RETURNING *', (brand, model))

 car = cursor.fetchone()

 connection.commit()

 cursor.close()
 connection.close()

 return jsonify(car), 201

# Route pour mettre à jour une voiture
@app.route('/cars/<int:id>', methods=['PUT'])
def updateOneCar(id):
 data = request.get_json()

 brand = data.get('brand')
 model = data.get('model')

 connection = get_connection()
 cursor = connection.cursor()

 if brand or model:

  if brand:
   cursor.execute('UPDATE car SET brand = %s WHERE car_id = %s RETURNING *', (brand, id,))
   updatedCar = cursor.fetchone()
   connection.commit()

  if model:
   cursor.execute('UPDATE car SET model = %s WHERE car_id = %s RETURNING *', (model, id,))
   updatedCar = cursor.fetchone()
   connection.commit()

  cursor.close()
  connection.close()

  return jsonify(updatedCar), 201
 
 else:
  return 'Aucune donnée soumise à mettre à jour', 400