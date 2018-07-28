import datetime

def calc_start_time(time: int, unit):
    now = datetime.datetime.now()
    if unit == "minutes":
        return now - datetime.timedelta(hours=0, minutes=time)
    elif unit == "hours":
        return now - datetime.timedelta(hours=time)

