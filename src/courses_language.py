import os

from pymongo import MongoClient, ASCENDING

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', 27017)
DB_NAME = os.environ.get('DB_NAME', 'paloma')


class DataBase():

    def client(self, collection):
        client = MongoClient(DB_HOST, DB_PORT)
        db = client[DB_NAME]
        return db[collection]


db = DataBase()

collection = 'courses_language'

courses = [
    {
        "name": "Duolingo",
        "based": ["exemplo", "exercicio_interativo"],
        "preco_real": [0.0],
        "preco-dolar": [0],
        "dinamica": ["curso_livre"],
        "plataforma": ["android_online", "ios_online"],
        "url": "https://www.duolingo.com/pt",
        "extra": ["comunicacao_alunos"],
        "descricao": "preecher",
    },
    {
        "name": "Memrise",
        "based": ["exemplo", "exercicio_interativo"],
        "preco_real": [0],
        "preco_dolar": [0, 9, 54],
        "dinamica": ["curso_livre"],
        "plataforma": ["android_online", "ios_online", "android_offline",
                       "ios_offline", "desktop_online", "desktop_offline"],
        "url": "https://www.memrise.com/",
        "extra": ["selecao_nivel", "comunicacao_alunos"],
        "descricao": "preecher",
    },
    {
        "name": "Live Mocha",
        "based": ["texto", "video_aula", "exemplo", "exercicio_interativo"],
        "preco_real": [0],
        "dinamica": ["curso_livre"],
        "plataforma": ["desktop_online"],
        "url": "http://livemocha.com/",
        "extra": ["selecao_nivel", "professor", "comunicacao_alunos"],
        "descricao": "preecher",
    },
    {
        "name": "IBEU",
        "based": ["texto", "video_aula", "exemplo", "exercicio_interativo"],
        "preco_real": [183],
        "dinamica": ["tempo_definido"],
        "plataforma": ["android_online", "ios_online", "desktop_online"],
        "url": "http://inglesonline.ibeu.org.br/site/",
        "extra": ["selecao_nivel", "professor", "comunicacao_alunos"],
        "descricao": "preecher",
    },
    {
        "name": "Busuu",
        "based": ["texto", "exemplo", "exercicio_interativo"],
        "preco_real": [0, 7, 9, 14, 24],
        "dinamica": ["curso_livre"],
        "plataforma": ["android_online", "ios_online", "desktop_online"],
        "url": "https://www.busuu.com/pt/",
        "extra": ["selecao_nivel", "comunicacao_alunos"],
        "descricao": "preecher",
    },
    {
        "name": "English Town",
        "based": ["texto", "video_aula", "exemplo", "exercicio_interativo"],
        "preco_real": [139, 210],
        "dinamica": ["curso_livre"],
        "plataforma": ["android_online", "ios_online", "desktop_online"],
        "url": "http://www.englishtown.com.br/",
        "extra": ["selecao_nivel", "professor", "comunicacao_alunos"],
        "descricao": "preecher",
    },
    {
        "name": "English Up",
        "based": ["texto", "video_aula", "exemplo", "exercicio_interativo"],
        "preco_real": [200, 300, 400, 500],
        "dinamica": ["tempo_definido"],
        "plataforma": ["desktop_online"],
        "url": "http://www.englishup.com.br/",
        "extra": ["selecao_nivel", "professor", "comunicacao_alunos"],
        "descricao": "preecher",
    },
    {
        "name": "UOL Curso de Ingles",
        "based": ["texto", "video_aula", "exemplo", "exercicio_interativo"],
        "preco_real": [39, 79],
        "dinamica": ["curso_livre", "tempo_definido"],
        "plataforma": ["desktop_online", "desktop_offline"],
        "url": "http://cursodeingles.uol.com.br/",
        "extra": ["selecao_nivel", "professor", "comunicacao_alunos"],
        "descricao": "preecher",
    },
    {
        "name": "Cursos 24 Horas",
        "based": ["texto", "video_aula", "exemplo", "exercicio_interativo"],
        "preco_real": [30],
        "dinamica": ["curso_livre", "tempo_definido"],
        "plataforma": ["desktop_online"],
        "url": "http://www.cursos24horas.com.br/",
        "extra": ["selecao_nivel", "professor", "comunicacao_alunos"],
        "descricao": "preecher",
    },
    {
        "name": "Prime cursos",
        "based": ["texto", "exemplo"],
        "preco_real": [0],
        "dinamica": ["curso_livre", "tempo_definido"],
        "plataforma": ["desktop_online"],
        "url": "https://www.primecursos.com.br",
        "extra": ["selecao_nivel"],
        "descricao": "preecher",
    },
    {
        "name": "Open english",
        "based": ["texto", "video_aula", "exemplo", "exercicio_interativo"],
        "preco_real": [147],
        "dinamica": ["curso_livre"],
        "plataforma": ["desktop_online"],
        "url": "http://www.openenglish.com.br/",
        "extra": ["selecao_nivel", "professor"],
        "descricao": "preecher",
    },
    {
        "name": "Ingles do Jerry",
        "based": ["video_aula", "exemplo"],
        "preco_real": [0, 134],
        "dinamica": ["curso_livre", "tempo_definido"],
        "plataforma": ["desktop_online", "desktop_offline"],
        "url": "http://inglesdojerry.com.br/",
        "extra": ["professor"],
        "descricao": "preecher",
    },
    {
        "name": "Babbel",
        "based": ["exemplo", "exercicio_interativo"],
        "preco_real": [12, 15, 23],
        "dinamica": ["curso_livre", "inicioDefinido"],
        "plataforma": ["desktop_online", "android_online"],
        "url": "https://pt.babbel.com/",
        "extra": ["selecao_nivel"],
        "descricao": "preecher",
    },
    {
        "name": "Iped idiomas",
        "based": ["video_aula"],
        "preco_real": [8, 12, 33],
        "dinamica": ["curso_livre", "tempo_definido"],
        "plataforma": ["desktop_online"],
        "url": "https://www.iped.com.br/idiomas",
        "extra": ["selecao_nivel", "comunicacao_alunos"],
        "descricao": "preecher",
    },
    {
        "name": "Ingles Curso",
        "based": ["texto", "video_aula", "exemplo", "exercicio_interativo"],
        "preco_real": [0],
        "dinamica": ["curso_livre"],
        "plataforma": ["desktop_online"],
        "url": "http://www.inglescurso.net.br/",
        "extra": ["selecao_nivel"],
        "descricao": "preecher",
    },
    {
        "name": "Aba English",
        "based": ["texto", "video_aula", "exemplo", "exercicio_interativo"],
        "preco_real": [0, 45, 58, 66, 90],
        "dinamica": ["curso_livre"],
        "plataforma": ["desktop_online", "android_online", "ios_online"],
        "url": "http://www.abaenglish.com/pt/",
        "extra": ["selecao_nivel", "professor"],
        "descricao": "preecher",
    },
    {
        "name": "Learn American English",
        "based": ["texto", "video_aula", "exemplo"],
        "preco_real": [0],
        "dinamica": ["curso_livre"],
        "plataforma": ["desktop_online"],
        "url": "http://www.learnamericanenglishonline.com/",
        "extra": ["selecao_nivel"],
        "descricao": "preecher",
    },
    {
        "name": "1- Language",
        "based": ["texto", "exemplo", "exercicio_interativo"],
        "preco_real": [0],
        "dinamica": ["curso_livre"],
        "plataforma": ["desktop_online"],
        "url": "http://www.1-language.com/",
        "extra": ["selecao_nivel"],
        "descricao": "preecher",
    },
    {
        "name": "Usa Learns",
        "based": ["texto", "video_aula", "exemplo", "exercicio_interativo"],
        "preco_real": [0, 6],
        "dinamica": ["curso_livre"],
        "plataforma": ["desktop_online", "android_online", "ios_online"],
        "url": "http://www.usalearns.org/",
        "extra": ["selecao_nivel"],
        "descricao": "preecher",
    },
    {
        "name": "Petra Lingua",
        "based": ["texto", "video_aula", "exemplo", "exercicio_interativo"],
        "preco_real": [89],
        "dinamica": ["curso_livre"],
        "plataforma": ["desktop_online", "desktop_offline",
                       "android_online", "android_offline", "ios_online", "ios_offline"],
        "url": "http://www.petralingua.com/pt/",
        "extra": [],
        "descricao": "preecher",
    },
    {
        "name": "5 minute english",
        "based": ["texto", "exemplo", "exercicio_interativo"],
        "preco_real": [0],
        "dinamica": ["curso_livre"],
        "plataforma": ["desktop_online"],
        "url": "http://www.5minuteenglish.com/",
        "extra": [],
        "descricao": "preecher",
    },
    {
        "name": "Anki",
        "based": ["texto", "exemplo"],
        "preco_real": [0],
        "dinamica": ["curso_livre"],
        "plataforma": ["desktop_online", "desktop_offline", "android_online",
                       "android_offline", "ios_online", "ios_offline"],
        "url": "http://ankisrs.net/",
        "extra": ["selecao_nivel"],
        "descricao": "preecher",
    },
    {
        "name": "Speaking Your Best Inc",
        "based": ["video_aula"],
        "preco_dolar": [125],
        "dinamica": ["curso_livre", "tempo_definido"],
        "plataforma": ["desktop_online", "desktop_offline"],
        "url": "http://www.speakingyourbest.com/",
        "extra": ["professor"],
        "descricao": "preecher",
    }
]

db.client(collection).remove({})

db.client(collection).create_index([('name', ASCENDING)], unique=True)

for course in courses:
    db.client(collection).insert_one(course)
