import os

from src.library.database.Mongo import Mongo
from src.model.preference.Preference import Preference


class PreferenceDao:
    def __init__(self):
        self.__mongo: Mongo = Mongo(
            host=os.getenv("MONGO_HOST"),
            port=int(os.getenv("MONGO_PORT")),
            default_db=os.getenv("MONGO_DEFAULT_DB")
        )
        self.__like_collection = "userLikeCollection"
        self.__dislike_collection = "userDislikeCollection"

    def add_like(self, preference: Preference):
        self.__mongo.insert_one(
            collection=self.__like_collection,
            elem={
                "user_id": preference.user_id,
                "product_id": preference.product_id
            }
        )

    def add_dislike(self, preference: Preference):
        self.__mongo.insert_one(
            collection=self.__dislike_collection,
            elem={
                "user_id": preference.user_id,
                "product_id": preference.product_id
            }
        )



    @staticmethod
    def __build_product(elem) -> Preference:
        return Preference(
            product_id=elem["product_id"],
            user_id=elem["user_id"]
        )