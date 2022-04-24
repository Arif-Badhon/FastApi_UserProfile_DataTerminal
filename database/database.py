from decouple import config
from .database_helper import user_helper, admin_helper
from bson import ObjectId
from pymongo import MongoClient

MONGO_DETAILS = config('MONGO_DETAILS')
port = 8000
client = MongoClient(MONGO_DETAILS, port)
db = client["DATATERMINAL_USER"]

user_collection = db.get_collection('user')
admin_collection = db.get_collection('admin')

def add_admin(admin_data: dict) -> dict:
    admin = admin_collection.insert_one(admin_data)
    new_admin = admin_collection.find_one({"_id": admin.inserted_id})
    return admin_helper(new_admin)


def retrieve_users():
    users = []
    for user in user_collection.find():
        users.append(user_helper(user))
    return users


def add_user(user_data: dict) -> dict:
    user = user_collection.insert_one(user_data)
    new_user = user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True

async def update_user_data(id: str, data: dict):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        user_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True