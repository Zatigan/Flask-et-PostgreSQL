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
  user='libadm1475',
  password='SP7c3$@uwL84jmSEoP3',
  port=5432,
  cursor_factory=RealDictCursor
 )

