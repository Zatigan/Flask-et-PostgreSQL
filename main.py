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

# Route pour l'accueil
@app.route('/')
def index():
 return 'Bienvenue dans mon API Flask'

# Route pour afficher tous les livres
@app.route('/books', methods=['GET'])
def get_book_list():
 connection = get_connection()
 cursor = connection.cursor()

 cursor.execute('SELECT * FROM book ORDER BY book_id')
 books = cursor.fetchall()

 cursor.close()
 connection.close()

 return jsonify(books)

# Route pour afficher un seul livre
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
 connection = get_connection()
 cursor = connection.cursor()

 cursor.execute('SELECT * FROM book WHERE book_id = %s', (id,))
 book = cursor.fetchone()

 cursor.close()
 connection.close()

 if book:
  return jsonify(book)
 else:
  return 'Livre non trouvé', 404