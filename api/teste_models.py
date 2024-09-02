import unittest
import sqlite3
from app import fetch_planets_data, fetch_characters_data, fetch_starships_data, store_planets_data, store_characters_data, store_starships_data
from models import get_hottest_planets, get_most_appearing_characters, get_fastest_starships

class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configuração inicial: cria o banco de dados em um arquivo e estabelece a conexão
        cls.db_name = 'test_star_wars.db'
        cls.conn = sqlite3.connect(cls.db_name)
        cls.create_tables()

    @classmethod
    def tearDownClass(cls):
        # Limpeza final: fecha a conexão e remove o arquivo de banco de dados após os testes
        cls.conn.close()
        import os
        os.remove(cls.db_name)

    @classmethod
    def create_tables(cls):
        # Criação das tabelas necessárias para os testes
        c = cls.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS planets
                     (name TEXT, climate TEXT, gravity TEXT, terrain TEXT, surface_water TEXT, population TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS characters
                     (name TEXT, height TEXT, mass TEXT, hair_color TEXT, skin_color TEXT, 
                      eye_color TEXT, birth_year TEXT, gender TEXT, appearances INTEGER)''')
        c.execute('''CREATE TABLE IF NOT EXISTS starships
                     (name TEXT, model TEXT, manufacturer TEXT, cost_in_credits TEXT, length TEXT, 
                      max_atmosphering_speed TEXT, crew TEXT, passengers TEXT, cargo_capacity TEXT)''')
        cls.conn.commit()

    def setUp(self):
        # Limpeza das tabelas antes de cada teste para garantir um estado consistente
        c = self.conn.cursor()
        c.execute('DELETE FROM planets')
        c.execute('DELETE FROM characters')
        c.execute('DELETE FROM starships')
        self.conn.commit()

    def test_store_planets_data(self):
        # Teste para verificar se os dados dos planetas estão sendo armazenados corretamente
        planets = [{'name': 'Tatooine', 'climate': 'arid', 'gravity': '1 standard', 'terrain': 'desert', 'surface_water': '1', 'population': '200000'}]
        store_planets_data(planets, self.conn)

        # Verificação: garantir que o planeta foi armazenado corretamente no banco de dados
        c = self.conn.cursor()
        c.execute('SELECT * FROM planets')
        result = c.fetchall()
        self.assertEqual(len(result), 1)  # Deve haver exatamente 1 planeta armazenado
        self.assertEqual(result[0][0], 'Tatooine')  # O nome do planeta deve ser 'Tatooine'
        print("Test 'test_store_planets_data' passed: ok")

    def test_store_characters_data(self):
        # Teste para verificar se os dados dos personagens estão sendo armazenados corretamente
        characters = [{'name': 'Luke Skywalker', 'height': '172', 'mass': '77', 'hair_color': 'blond', 'skin_color': 'fair', 
                        'eye_color': 'blue', 'birth_year': '19BBY', 'gender': 'male', 'films': ['A New Hope'] }]
        store_characters_data(characters, self.conn)

        # Verificação: garantir que o personagem foi armazenado corretamente no banco de dados
        c = self.conn.cursor()
        c.execute('SELECT * FROM characters')
        result = c.fetchall()
        self.assertEqual(len(result), 1)  # Deve haver exatamente 1 personagem armazenado
        self.assertEqual(result[0][0], 'Luke Skywalker')  # O nome do personagem deve ser 'Luke Skywalker'
        print("Test 'test_store_characters_data' passed: ok")

    def test_store_starships_data(self):
        # Teste para verificar se os dados das naves estelares estão sendo armazenados corretamente
        starships = [{'name': 'X-wing', 'model': 'T-65 X-wing', 'manufacturer': 'Incom T-65', 'cost_in_credits': '149999', 
                      'length': '12.5', 'max_atmosphering_speed': '1050', 'crew': '1', 'passengers': '0', 'cargo_capacity': '110'}]
        store_starships_data(starships, self.conn)

        # Verificação: garantir que a nave estelar foi armazenada corretamente no banco de dados
        c = self.conn.cursor()
        c.execute('SELECT * FROM starships')
        result = c.fetchall()
        self.assertEqual(len(result), 1)  # Deve haver exatamente 1 nave estelar armazenada
        self.assertEqual(result[0][0], 'X-wing')  # O nome da nave deve ser 'X-wing'
        print("Test 'test_store_starships_data' passed: ok")

    def test_get_hottest_planets(self):
        # Teste para verificar se a função get_hottest_planets retorna o planeta com o clima mais quente corretamente
        planets = [{'name': 'Hoth', 'climate': 'frozen', 'gravity': '1', 'terrain': 'ice caves', 'surface_water': '100', 'population': 'unknown'}]
        store_planets_data(planets, self.conn)
        hottest_planets = get_hottest_planets(self.conn)

        # Verificação: garantir que o planeta mais quente seja retornado corretamente
        self.assertEqual(len(hottest_planets), 1)  # Deve haver exatamente 1 planeta retornado
        self.assertEqual(hottest_planets[0][0], 'Hoth')  # O nome do planeta deve ser 'Hoth'
        print("Test 'test_get_hottest_planets' passed: ok")

    def test_get_most_appearing_characters(self):
        # Teste para verificar se a função get_most_appearing_characters retorna o personagem com mais aparições corretamente
        characters = [{'name': 'Darth Vader', 'height': '202', 'mass': '136', 'hair_color': 'none', 'skin_color': 'white', 
                        'eye_color': 'yellow', 'birth_year': '41.9BBY', 'gender': 'male', 'films': ['A New Hope', 'The Empire Strikes Back']}]
        store_characters_data(characters, self.conn)
        most_appearing_characters = get_most_appearing_characters(self.conn)

        # Verificação: garantir que o personagem com mais aparições seja retornado corretamente
        self.assertEqual(len(most_appearing_characters), 1)  # Deve haver exatamente 1 personagem retornado
        self.assertEqual(most_appearing_characters[0][0], 'Darth Vader')  # O nome do personagem deve ser 'Darth Vader'
        print("Test 'test_get_most_appearing_characters' passed: ok")

    def test_get_fastest_starships(self):
        # Teste para verificar se a função get_fastest_starships retorna a nave mais rápida corretamente
        starships = [{'name': 'Millennium Falcon', 'model': 'YT-1300 Corellian Freighter', 'manufacturer': 'Corellian Engineering Corporation', 
                      'cost_in_credits': '100000', 'length': '34.37', 'max_atmosphering_speed': '1050', 'crew': '4', 'passengers': '6', 
                      'cargo_capacity': '100000'}]
        store_starships_data(starships, self.conn)
        fastest_starships = get_fastest_starships(self.conn)

        # Verificação: garantir que a nave mais rápida seja retornada corretamente
        self.assertEqual(len(fastest_starships), 1)  # Deve haver exatamente 1 nave retornada
        self.assertEqual(fastest_starships[0][0], 'Millennium Falcon')  # O nome da nave deve ser 'Millennium Falcon'
        print("Test 'test_get_fastest_starships' passed: ok")

if __name__ == '__main__':
    unittest.main()
