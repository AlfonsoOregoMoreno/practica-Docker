from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Conexión a la base de datos PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host="db",        # Nombre del servicio del contenedor de PostgreSQL
        database="counter_db",
        user="postgres",
        password="postgres"
    )
    return conn

# Inicializa la base de datos (solo si es necesario)
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS counter (
                        id SERIAL PRIMARY KEY,
                        count INTEGER NOT NULL
                      );''')
    cursor.execute('''INSERT INTO counter (count) VALUES (0)
                      ON CONFLICT (id) DO NOTHING;''')
    conn.commit()
    cursor.close()
    conn.close()

# Ruta para incrementar el contador
@app.route('/increment', methods=['GET'])
def increment():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE counter SET count = count + 1 RETURNING count;')
    count = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(count=count)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=os.environ['FLASK_APP_CONTAINER_EXPOSED_PORT'])
