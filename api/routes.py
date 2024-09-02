from flask import jsonify
from databases import create_connection
from models import get_hottest_planets_model, get_most_appearing_characters_model, get_fastest_starships_model

# Módulo para definir as rotas da API

def setup_routes(app):
    @app.route('/hottest_planet')
    def hottest_planet():
        conn = create_connection('star_wars.db')
        hottest = get_hottest_planets_model(conn)
        conn.close()
        result = [{'name': planet[0], 'climate': planet[1], 'gravity': planet[2], 
                   'terrain': planet[3], 'surface_water': planet[4], 'population': planet[5]} 
                  for planet in hottest]
        return jsonify(result)

    @app.route('/appears_most')
    def appears_most():
        conn = create_connection('star_wars.db')
        most_appearing = get_most_appearing_characters_model(conn)
        conn.close()
        result = [{'name': character[0], 'height': character[1], 'mass': character[2], 
                   'hair_color': character[3], 'skin_color': character[4], 'eye_color': character[5], 
                   'birth_year': character[6], 'gender': character[7], 'appearances': character[8]} 
                  for character in most_appearing]
        return jsonify(result)

    @app.route('/fastest_ships')
    def fastest_ships():
        conn = create_connection('star_wars.db')
        fastest = get_fastest_starships_model(conn)
        conn.close()
        result = [{'name': starship[0], 'model': starship[1], 'manufacturer': starship[2], 
                   'cost_in_credits': starship[3], 'length': starship[4], 
                   'max_atmosphering_speed': starship[5], 'crew': starship[6], 
                   'passengers': starship[7], 'cargo_capacity': starship[8]} 
                  for starship in fastest]
        return jsonify(result)
