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
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            user_id TEXT not null ,
            session_id TEXT not null,
            place TEXT,
            start_time INTEGER,
            free_period INTEGER,
            payment_per_hour INTEGER,
            stage_id TEXT,
            closed INTEGER
          )
        ''')
    db.commit()
    db.close()


def insert(user_id="", session_id="", place="", start_time="", free_period="", payment_per_hour="", closed_status=0):
    if user_id == "":
        raise Exception("user_id is null")

    db = get_db()
    c = db.cursor()
    c.execute('''
        INSERT INTO PARKING (user_id, session_id, place, start_time, free_period, payment_per_hour, stage_id, closed)
        VALUES (?,?,?,?,?,?, NULL, ?)
    ''', 
    (
        user_id,
        session_id,
        place, 
        start_time,
        free_period,
        payment_per_hour,
        closed_status
        ))
    db.commit()
    db.close()

def update_place(place, id_s):
    db = get_db()
    c = db.cursor()
    c.execute('''
    UPDATE PARKING
    SET place = ?
    WHERE id=?
    ''', (place, _id))

    db.commit()
    db.close()

def update_start_time(start_time, id_s):
    db = get_db()
    c = db.cursor()
    c.execute('''
    UPDATE PARKING
    SET start_time = ?
    WHERE id=?
    ''', (start_time, id_s))

    db.commit()
    db.close()
    return 0

def update_free_period(free_period, id_s):
    db = get_db()
    c = db.cursor()
    c.execute('''
    UPDATE PARKING
    SET free_period = ?
    WHERE id=?;
    ''', (free_period, id_s ))

    db.commit()
    db.close()

def update_payment_per_hour(payment_per_hour, id_s):
    db = get_db()
    c = db.cursor()
    c.execute('''
    UPDATE PARKING
    SET payment_per_hour = ?
    WHERE id=?
    ''', (payment_per_hour, id_s))
    db.commit()
    db.close()

def update_close_status(id_s):
    db = get_db()
    c = db.cursor()
    c.execute('''
    UPDATE PARKING
    SET closed = 1
    WHERE id=?;
    ''', (id_s))
    db.commit()
    db.close()

def select_all_data(user_id, session_id):
    db = get_db()
    c = db.cursor()
    c.execute('''
    SELECT id, user_id, session_id, place, start_time, free_period, payment_per_hour, stage_id, closed from PARKING
    WHERE  id = (SELECT MAX(id) FROM PARKING WHERE session_id=? AND user_id=? and closed=0);
    ''', (session_id, user_id))

    data = c.fetchall()[0]

    if len(data) == 0:
        return None

    return {
        'id': data[0],
        'user_id': data[1],
        'session_id': data[2],
        'place': data[3],
        'start_time': data[4],
        'free_period': data[5],
        'payment_per_hour': data[6],
        'stage_id': data[7],
        'closed': data[8],
        }

