import sqlite3
import unittest
from databases import create_connection, store_planets_data, store_characters_data, store_starships_data, get_hottest_planets, get_most_appearing_characters, get_fastest_starships
from data_fetchers import fetch_planets_data, fetch_characters_data, fetch_starships_data

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Configuração inicial: cria um banco de dados em memória para cada teste, garantindo que os testes sejam independentes.
        self.conn = sqlite3.connect(':memory:')
        self.create_tables()

    def tearDown(self):
        # Fecha a conexão com o banco de dados após cada teste.
        self.conn.close()

    def create_tables(self):
        # Cria as tabelas necessárias para armazenar dados de planetas, personagens e naves.
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS planets
                     (name TEXT, climate TEXT, gravity TEXT, terrain TEXT, surface_water TEXT, population TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS characters
                     (name TEXT, height TEXT, mass TEXT, hair_color TEXT, skin_color TEXT, 
                      eye_color TEXT, birth_year TEXT, gender TEXT, appearances INTEGER)''')
        c.execute('''CREATE TABLE IF NOT EXISTS starships
                     (name TEXT, model TEXT, manufacturer TEXT, cost_in_credits TEXT, length TEXT, 
                      max_atmosphering_speed TEXT, crew TEXT, passengers TEXT, cargo_capacity TEXT)''')

    def test_store_planets_data(self):
        # Objetivo: Verificar se os dados dos planetas são armazenados corretamente no banco de dados.
        planets = fetch_planets_data()  # Obtém dados de planetas
        store_planets_data(planets, self.conn)  # Armazena os dados no banco

        # Verifica se os dados foram inseridos na tabela de planetas
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM planets')
        result = cursor.fetchall()
        
        # Testa se há pelo menos um planeta armazenado
        self.assertGreater(len(result), 0)
        print("Test 'test_store_planets_data' passed: ok")

    def test_store_characters_data(self):
        # Objetivo: Verificar se os dados dos personagens são armazenados corretamente no banco de dados.
        characters = fetch_characters_data()  # Obtém dados de personagens
        store_characters_data(characters, self.conn)  # Armazena os dados no banco

        # Verifica se os dados foram inseridos na tabela de personagens
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM characters')
        result = cursor.fetchall()
        
        # Testa se há pelo menos um personagem armazenado
        self.assertGreater(len(result), 0)
        print("Test 'test_store_characters_data' passed: ok")

    def test_store_starships_data(self):
        # Objetivo: Verificar se os dados das naves espaciais são armazenados corretamente no banco de dados.
        starships = fetch_starships_data()  # Obtém dados de naves espaciais
        store_starships_data(starships, self.conn)  # Armazena os dados no banco

        # Verifica se os dados foram inseridos na tabela de naves espaciais
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM starships')
        result = cursor.fetchall()
        
        # Testa se há pelo menos uma nave armazenada
        self.assertGreater(len(result), 0)
        print("Test 'test_store_starships_data' passed: ok")

    def test_get_hottest_planets(self):
        # Objetivo: Verificar se a função que retorna os planetas com o clima mais quente está funcionando corretamente.
        planets = fetch_planets_data()  # Obtém dados de planetas
        store_planets_data(planets, self.conn)  # Armazena os dados no banco

        # Obtém os planetas mais quentes do banco de dados
        hottest = get_hottest_planets(self.conn)
        
        # Testa se há pelo menos um planeta na lista de planetas mais quentes
        self.assertGreater(len(hottest), 0)
        print("Test 'test_get_hottest_planets' passed: ok")

    def test_get_most_appearing_characters(self):
        # Objetivo: Verificar se a função que retorna os personagens que mais aparecem nos filmes está funcionando corretamente.
        characters = fetch_characters_data()  # Obtém dados de personagens
        store_characters_data(characters, self.conn)  # Armazena os dados no banco

        # Obtém os personagens que mais aparecem
        most_appearing = get_most_appearing_characters(self.conn)
        
        # Testa se há pelo menos um personagem na lista de personagens que mais aparecem
        self.assertGreater(len(most_appearing), 0)
        print("Test 'test_get_most_appearing_characters' passed: ok")

    def test_get_fastest_starships(self):
        # Objetivo: Verificar se a função que retorna as naves mais rápidas está funcionando corretamente.
        starships = fetch_starships_data()  # Obtém dados de naves espaciais
        store_starships_data(starships, self.conn)  # Armazena os dados no banco

        # Obtém as naves mais rápidas
        fastest = get_fastest_starships(self.conn)
        
        # Testa se há pelo menos uma nave na lista das naves mais rápidas
        self.assertGreater(len(fastest), 0)
        print("Test 'test_get_fastest_starships' passed: ok")

if __name__ == '__main__':
    unittest.main()
