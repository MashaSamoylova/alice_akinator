import datetime
import time
from db_manager import *

def calc_start_time(time_s: int, unit):
    now = int(time.time())
    if unit == "minutes":
        print(now, time_s*60)
        return now - time_s*60
    elif unit == "hours":
        return now - time_s*3600

def calc_free_time(user_id, session_id):
    data = select_all_data(user_id, session_id)
    start_time = data['start_time']
    free_time = data['free_period']
    print(free_time - (int(time.time()) - start_time)//60)
    return free_time - (int(time.time()) - start_time)//60
    
def calc_payment(user_id, session_id):
    data = select_all_data(user_id, session_id)
    start_time = data['start_time']
    free_time = data['free_period']
    payment_per_hour = data['payment_per_hour']
    return (((int(time.time()) - start_time)//60 - free_time)/60)*payment_per_hour


