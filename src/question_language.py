# -*- coding: utf-8 -*-
import os

from pymongo import MongoClient

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', 27017)
DB_NAME = os.environ.get('DB_NAME', 'paloma')


class DataBase():

    def client(self, collection):
        client = MongoClient(DB_HOST, DB_PORT)
        db = client[DB_NAME]
        return db[collection]


db = DataBase()

collection = 'questions_language'

questions = [
    {
        'based': [
            {'texto': 'Textos'},
            {'video_aula': 'Video aulas'},
            {'exemplo': 'Examplos'},
            {'exercicio_interativo': 'Exercicios interativos'}
        ],
        'price': [
            {'gratis': 'Grátis'},
            {'ate30': 'Até 30 reais'},
            {'31a60': 'De 31 a 60 reais'},
            {'61a100': 'De 61 a 100 reais'},
            {'101a150': 'De 101 a 150 reais'},
            {'151mais': 'Mais de 151 reais'}
        ],
        'dynamic': [
            {'curso_livre': 'Curso Livre'},
            {'tempo_definido': 'Tempo de Curso Definido'},
            {'inicio_definido': 'Data de Início Definida'}
        ],
        'platform': [
            {'android_offline': 'Android - Offline'},
            {'android_online': 'Android - Online'},
            {'ios_offline': 'IOS - Offline'},
            {'ios_online': 'IOS - Online'},
            {'desktop_offline': 'Desktop - Offline'},
            {'desktop_online': 'Desktop - Online'}
        ],
        'extra': [
            {'selecao_nivel': 'Seleção de Nível de conhecimento'},
            {'professor': 'Professor Disponível'},
            {'comunicacao_alunos': 'Comunicação entre alunos'}
        ]
    }
]

db.client(collection).remove({})

for question in questions:
    db.client(collection).insert_one(question)
