from datetime import datetime
import random


def generate_random_time(start_date:datetime, end_date:datetime):
    start = int(start_date.timestamp())
    end = int(end_date.timestamp())
    random_time = random.randint(start, end)
    return datetime.fromtimestamp(random_time)
