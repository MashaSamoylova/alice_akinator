INSERT INTO PARKING (user_id, session_id, place, start_time, free_period, payment_per_hour)
VALUES ('111', '222', 'Гринвич Г9', '2018-07-28T20:00:00', 60, 10000);

UPDATE PARKING
SET place = ?
WHERE session_id=? AND user_id=?;

UPDATE PARKING
SET start_time = ?
WHERE session_id=? AND user_id=?;

UPDATE PARKING
SET free_period = ?
WHERE session_id=? AND user_id=?;

UPDATE PARKING
SET payment_per_hour = ?
WHERE session_id=? AND user_id=?;