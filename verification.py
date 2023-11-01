import time
import os
import asyncio
from utils import temp
from database.verify import *
from info import TOKEN_TIMEOUT
import random
import string

async def generate_random_string(length):
    characters = string.ascii_letters
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


async def get_current_time():
    return time.time()

async def get_readable_time(seconds):
    seconds = int(seconds)  # Convert seconds to an integer
    periods = [('d', 86400), ('h', 3600), ('m', 60), ('s', 1)]
    result = ''
    for period_name, period_seconds in periods:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            result += f'{int(period_value)}{period_name}'
    return result

async def checking_access(user_id):
    t = await get_current_time()
    user = await verify_user(user_id)
    time = user["time"]
    if time is None or t - time > TOKEN_TIMEOUT:
        return f"Dummy"
    else:
        return None
