import unittest
from app import app

class TestRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configuração inicial: Cria um cliente de teste para fazer requisições à aplicação
        cls.client = app.test_client()
        cls.client.testing = True  

    def test_hottest_planet_route(self):
        # Teste para verificar se a rota '/hottest_planet' retorna corretamente os dados
        response = self.client.get('/hottest_planet')
        
        # Verificação: O status da resposta deve ser 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Verificação: A resposta deve ser do tipo JSON, e esperamos uma lista
        self.assertIsInstance(response.json, list)
        
        print("Test 'hottest_planet_route' passed: ok")

    def test_appears_most_route(self):
        
        response = self.client.get('/appears_most')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        print("Test 'appears_most_route' passed: ok")

    def test_fastest_ships_route(self):
        
        response = self.client.get('/fastest_ships')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        print("Test 'fastest_ships_route' passed: ok")

if __name__ == '__main__':
    unittest.main()
