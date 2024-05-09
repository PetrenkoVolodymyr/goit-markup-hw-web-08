
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ukrcima:567234@mymongo.bpoqivq.mongodb.net/?retryWrites=true&w=majority&appName=MyMongo"


client = MongoClient(uri, server_api=ServerApi('1'))

db = client.webdb


try:
    db.cats.insert_many([
    {
        "name": 'L111ama',
        "age": 2,
        "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
    },
    {
        "name": 'Li222za',
        "age": 4,
        "features": ['ходить в лоток', 'дає себе гладити', 'білий'],
    },
    ])
except Exception as e:
    print(e)




