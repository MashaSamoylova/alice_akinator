import datetime

def calc_start_time(time: int, unit):
    now = datetime.datetime.now()
    if unit == "minutes":
        return now - datetime.timedelta(hours=1, minutes=23))


if __name__=="__main__":
    calc_start_time(5, "minutes")
