from pymongo import MongoClient


class Mongo:
    def __init__(self, host: str, port: int, default_db: str):
        self.__client = MongoClient(
            host=host,
            port=port
        )
        self.__database = self.__client[default_db]

    def find_all(self, collection: str):
        db_collection = self.__database[collection]
        for elem in db_collection.find():
            yield elem

    def find_by(self, collection: str, field: dict):
        db_collection = self.__database[collection]
        for elem in db_collection.find(field):
            yield elem

    def insert_one(self, collection: str, elem: dict):
        db_collection = self.__database[collection]
        db_collection.insert_one(elem)

if __name__ == '__main__':
    mongo = MongoClient(
        host="localhost",
        port=27018
    )
    db = mongo["userPreferences"]
    likes = db["userLikeCollection"]

    for elem in likes.find():
        print(elem)

    dislikes = db["userDislikeCollection"]

    print("\n")
    for elem in dislikes.find():
        print(elem)
