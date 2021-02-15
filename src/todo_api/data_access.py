"""Data access layer for Mongodb."""
import pymongo


class Database:
    """Database wrapper."""
    client = None

    @staticmethod
    def get_client() -> pymongo.MongoClient:
        """Returns a pymongo.MongoClient object."""
        if Database.client is None:
            Database.client = pymongo.MongoClient(host=None, port=None)

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
