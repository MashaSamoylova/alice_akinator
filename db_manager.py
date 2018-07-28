import sqlite3
import json

DB_NAIM = "data.db"

def get_db():
    return sqlite3.connect(DB_NAIM)

def prepare_db():
    db = get_db()
    c = db.cursor()
    c.execute(
            '''
            create table if not exists PARKING (
            user_id TEXT PRIMARY KEY,
            session_id TEXT not null,
            place TEXT,
            start_time TEXT,
            free_period INTEGER,
            payment_per_hour INTEGER
          )
        ''')
    db.commit()
    db.close()
    return 0


def insert(user_id="", session_id="", place="", start_time="", free_period="", payment_per_hour=""):
    if user_id == "":
        raise Exception("user_id is null")

    db = get_db()
    c = db.cursor()
    c.execute('''
        INSERT INTO PARKING (user_id, session_id, place, start_time, free_period, payment_per_hour)
        VALUES (?,?,?,?, ?,?)
    ''', 
    (
        user_id,
        session_id,
        place, 
        start_time,
        free_period,
        payment_per_hour,
        ))
    db.commit()
    db.close()
    
    return 0

def update_place(user_id, session_id, place):
    db = get_db()
    c = db.cursor()
    c.execute('''
    UPDATE PARKING
    SET place = ?
    WHERE session_id=? AND user_id=?
    ''', (place, session_id, user_id))

    db.commit()
    db.close()
    return 0

def update_start_time(user_id, session_id, start_time):
    db = get_db()
    c = db.cursor()
    c.execute('''
    UPDATE PARKING
    SET start_time = ?
    WHERE session_id=? AND user_id=?
    ''', (start_time, session_id, user_id))

    db.commit()
    db.close()
    return 0

def update_free_period(user_id, session_id, free_period):
    db = get_db()
    c = db.cursor()
    c.execute('''
    UPDATE PARKING
    SET free_period = ?
    WHERE session_id=? AND user_id=?;
    ''', (free_period, session_id, user_id))

    db.commit()
    db.close()
    return 0

def update_payment_per_hour(user_id, session_id, payment_per_hour):
    db = get_db()
    c = db.cursor()
    c.execute('''
    UPDATE PARKING
    SET payment_per_hour = ?
    WHERE session_id=? AND user_id=?;
    ''', (payment_per_hour, session_id, user_id))

    db.commit()
    db.close()
    return 0

def select_all_data(user_id, session_id):
    db = get_db()
    c = db.cursor()
    c.execute('''
    SELECT place, start_time, free_period, payment_per_hour from PARKING
    WHERE session_id=? AND user_id=?;
    ''', (session_id, user_id))

    data = c.fetchall()[0]

    return {
        'place': data[0],
        'start_time': data[1],
        'free_period': data[2],
        'payment_per_hour': data[3],
        }


