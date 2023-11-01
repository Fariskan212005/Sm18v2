from motor.motor_asyncio import AsyncIOMotorClient
from info import DATABASE_URI, DATABASE_NAME

client_verify = AsyncIOMotorClient(DATABASE_URI)
db_verify = client_verify[DATABASE_NAME]
col_verify = db_verify["verify"]


async def verify_user(user_id):

    user_id = int(user_id)

    user = await col_verify.find_one({"user_id": user_id})

    if not user:
        res = {
            "user_id": user_id,
            "token": None,
            "time": None,
            "vtoken": None,
        }

        user = await col_verify.insert_one(res)

    return user

async def verify_user_data(user_id, value:dict):
    user_id = int(user_id)
    myquery = {"user_id": user_id}
    newvalues = { "$set": value }
    await col_verify.update_one(myquery, newvalues)

