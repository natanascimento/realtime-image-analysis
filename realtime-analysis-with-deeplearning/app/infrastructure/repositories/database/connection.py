import pymongo
from app.core.config import settings


class DatabaseConnection:

    @staticmethod
    def __get_connection_string() -> str:
        __connection_string = "{}://{}:{}@{}/{}?retryWrites=true&w=majority"
        return __connection_string.format(settings.DB_TYPE, 
                                        settings.DB_USER,
                                        settings.DB_PASSWORD,
                                        settings.DB_CLUSTER,
                                        settings.DB_NAME)

    def __set_database_connection(self, collection: str):
        __client = pymongo.MongoClient(self.__get_connection_string(), 
                                       serverSelectionTimeoutMS=5000)
        __database = __client[str(settings.DB_NAME)][collection]
        return __database

    def connect(self, collection: str):
        try:
            return self.__set_database_connection(collection=collection)
        except Exception as exception:
            print(f"[ERROR] The data producer has an error: \n{exception}")
