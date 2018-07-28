import datetime
import time
from db_manager import *

def calc_start_time(time: int, unit):
    now = int(time.time())
    if unit == "minutes":
        return now - unit*60
    elif unit == "hours":
        return now - unit*3600


def calc_free_time(user_id, session_id):
    data = select_all_data(user_id, session_id)
    start_time = data['start_time']
    free_time = data['free_time']
    return free_time - (int(time.time()) - start_time)//60
    
def calc_payment(user_id, session_id):
