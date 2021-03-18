from pymongo import MongoClient

try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['coffeestore']
    print('Connected...')
except Exception as e:
    print(e.message)