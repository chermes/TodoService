"""Data access layer for Mongodb."""
import os

import pymongo


class Database:
    """Database wrapper."""
    client = None

    @staticmethod
    def get_client() -> pymongo.MongoClient:
        """Returns a pymongo.MongoClient object."""
        host = os.getenv("MONGO_DB_URL")
        port = int(os.getenv("MONGO_DB_PORT", default="27017"))

        if host is None:
            raise EnvironmentError("Environment variable MONGO_DB_URL is not set")

        if Database.client is None:
            Database.client = pymongo.MongoClient(host=host, port=port)

        return Database.client


def get_db():
    """Returns the Mongo database."""
    client = Database.get_client()
    database = client.todo_database
    return database


def get_user_collection():
    """Returns the user collection."""
    database = get_db()
    coll = database.user_collection
    return coll


def get_items_collection():
    """Returns the items collection."""
    database = get_db()
    coll = database.items_collection
    return coll
