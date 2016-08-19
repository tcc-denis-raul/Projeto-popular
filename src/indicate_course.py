# -*- coding: utf-8 -*-
# Coleção para salvar os cursos indicado pelo usuário
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

collection = 'indicate_courses'

db.client(collection).remove({})

db.client(collection).ensure_index('url', unique=True)
