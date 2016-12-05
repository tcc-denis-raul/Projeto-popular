# -*- coding: utf-8 -*-
# cursos disponiveis para os usuários: para o tcc estaremos trabalhando apenas com o curso de ingles
import os

from pymongo import MongoClient

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', 27017)
DB_NAME = os.environ.get('DB_NAME', 'paloma')


class DataBase():

    def client(self, collection):
        client = MongoClient(DB_HOST, int(DB_PORT))
        db = client[DB_NAME]
        return db[collection]


db = DataBase()

collection = 'courses'

language = {
    'language': ['ingles']
}

db.client(collection).remove({})

db.client(collection).insert_one(language)
