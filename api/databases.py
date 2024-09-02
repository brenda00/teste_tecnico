import sqlite3

# Módulo para interações com o banco de dados

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def store_planets_data(planets, conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS planets
                 (name TEXT, climate TEXT, gravity TEXT, terrain TEXT, surface_water TEXT, population TEXT)''')
    for planet in planets:
        c.execute('''INSERT INTO planets (name, climate, gravity, terrain, surface_water, population)
                     VALUES (?, ?, ?, ?, ?, ?)''',
                     (planet['name'], planet['climate'], planet['gravity'], planet['terrain'], 
                      planet['surface_water'], planet['population']))
    conn.commit()

def store_characters_data(characters, conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS characters
                 (name TEXT, height TEXT, mass TEXT, hair_color TEXT, skin_color TEXT, 
                  eye_color TEXT, birth_year TEXT, gender TEXT, appearances INTEGER)''')
    for character in characters:
        c.execute('''INSERT INTO characters (name, height, mass, hair_color, skin_color, eye_color, 
                                             birth_year, gender, appearances)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (character['name'], character['height'], character['mass'], character['hair_color'], 
                      character['skin_color'], character['eye_color'], character['birth_year'], 
                      character['gender'], len(character['films'])))
    conn.commit()

def store_starships_data(starships, conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS starships
                 (name TEXT, model TEXT, manufacturer TEXT, cost_in_credits TEXT, length TEXT, 
                  max_atmosphering_speed TEXT, crew TEXT, passengers TEXT, cargo_capacity TEXT)''')
    for starship in starships:
        c.execute('''INSERT INTO starships (name, model, manufacturer, cost_in_credits, length, 
                                            max_atmosphering_speed, crew, passengers, cargo_capacity)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (starship['name'], starship['model'], starship['manufacturer'], starship['cost_in_credits'], 
                      starship['length'], starship['max_atmosphering_speed'], starship['crew'], 
                      starship['passengers'], starship['cargo_capacity']))
    conn.commit()

def get_hottest_planets(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM planets ORDER BY surface_water DESC LIMIT 3")
    return cursor.fetchall()

def get_most_appearing_characters(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM characters ORDER BY appearances DESC LIMIT 5")
    return cursor.fetchall()

def get_fastest_starships(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM starships ORDER BY max_atmosphering_speed DESC LIMIT 3")
    return cursor.fetchall()
