from app.infrastructure.repositories.database.connection import DatabaseConnection


class DataConsumer:

    def __init__(self, connection: DatabaseConnection) -> None:
        self.__database_connection = connection
        self.__connection = self.__database_connection.connect(collection="people-detection")

    def consume_last_insert(self):
        try:
            return self.__connection.find(sort=[("_id", -1)], limit=1)[0]
        except Exception as exception:
            print(f"[ERROR] The data consumer has an error: \n{exception}")

    def consume(self):
        try:
            return {"data": [{"location": result.get("location"),
                              "quantity": result.get("quantity"),
                              "detected_at": result.get("detected_at")} for result in self.__connection.find()]}
        except Exception as exception:
            print(f"[ERROR] The data consumer has an error: \n{exception}")
