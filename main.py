from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

def get_connection():
 return psycopg2.connect(
  host='localhost',
  database='flask_library',
  user='libadm1475',
  password='Secret-Postgres-Password42',
  port=5432,
  cursor_factory=RealDictCursor
 )

@app.route(('/'))
def index():
 return 'Bienvenue dans mon API Flask'