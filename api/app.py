from flask import Flask
import webbrowser
from data_fetchers import fetch_planets_data, fetch_characters_data, fetch_starships_data
from databases import create_connection, store_planets_data, store_characters_data, store_starships_data
from routes import setup_routes

# Arquivo principal que configura e executa a aplicação Flask

app = Flask(__name__)

# Configura as rotas
setup_routes(app)

if __name__ == '__main__':
    conn = create_connection('star_wars.db')

    # Coleta e armazena os dados
    planets = fetch_planets_data()
    store_planets_data(planets, conn)

    characters = fetch_characters_data()
    store_characters_data(characters, conn)

    starships = fetch_starships_data()
    store_starships_data(starships, conn)

    conn.close()

    #Abre direcionando no primeiro endpoint sobre o retorno dos planetas
    webbrowser.open_new('http://127.0.0.1:5000/hottest_planet')
    app.run(debug=True)
