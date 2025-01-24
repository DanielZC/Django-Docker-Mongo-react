import json
from django.conf import settings
from pymongo import MongoClient


class ConnectionDB:

    def __init__(self):
        self.db_settings = settings.DB_VARS
        self.db_name = self.db_settings["NAME"]
        self.db_user = self.db_settings["USER"]
        self.db_pws = self.db_settings["PASSWORD"]
        self.db_host = self.db_settings["HOST"]
        self.db_port = self.db_settings["PORT"]

        self.connection = self.get_connection()

    def get_db_connection_vars(self):

        return self.db_name, self.db_user, self.db_pws, self.db_host, self.db_port

    def db_ping(self):

        try:
            client = MongoClient(
                host=self.db_host,
                port=int(self.db_port),
                username=self.db_user,
                password=self.db_pws,
            )
            client.admin.command("ping")
            return "Conexión exitosa a MongoDB"
        except Exception as e:
            return f"Error al conectar a MongoDB: {str(e)}"

    def get_connection(self):
        mongo_client = MongoClient(
            host=self.db_host,
            port=int(self.db_port),
            username=self.db_user,
            password=self.db_pws,
        )

        return mongo_client

    def get_collection(self, collection_name):
        return self.connection[self.db_name][collection_name]

    def insert_one(self, collection_name, document):
        collection = self.get_collection(collection_name)
        return collection.insert_one(document)

    def insert_many(self, collection_name, documents):
        collection = self.get_collection(collection_name)
        return collection.insert_many(documents)

    def find_one(self, collection_name, query=None):
        collection = self.get_collection(collection_name)
        return collection.find_one(query)

    def find(self, collection_name, query=None):
        collection = self.get_collection(collection_name)
        result = collection.find(query)
        list_results = list(result)
        data = json.loads(json.dumps(list_results, indent=4, default=str))
        return data

    def update_one(self, collection_name, filter, update):
        collection = self.get_collection(collection_name)
        result = collection.update_one(filter, update)
        return result

    def update_many(self, collection_name, filter, update_pipeline):
        collection = self.get_collection(collection_name)
        return collection.update_many(filter, update_pipeline)

    def aggregate(self, collection_name, pipeline):
        collection = self.get_collection(collection_name)
        result = collection.aggregate(pipeline)
        list_results = list(result)
        return list_results

    def delete_many(self, collection_name, filter):
        collection = self.get_collection(collection_name)
        return collection.delete_many(filter)
