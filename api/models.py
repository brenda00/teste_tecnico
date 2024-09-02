from databases import get_hottest_planets, get_most_appearing_characters, get_fastest_starships

# Módulo para definir as funções de processamento dos dados

def get_hottest_planets_model(conn):
    return get_hottest_planets(conn)

def get_most_appearing_characters_model(conn):
    return get_most_appearing_characters(conn)

def get_fastest_starships_model(conn):
    return get_fastest_starships(conn)
