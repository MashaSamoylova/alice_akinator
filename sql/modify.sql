INSERT INTO PARKING (user_id, session_id, place, start_time, free_period, payment_per_hour, stage_id, closed)
VALUES ('111', '222', 'Гринвич Г91', '2018-07-28T20:00:00', 60, 10000, null, 0);

UPDATE PARKING
SET place = ?
WHERE id=?;

UPDATE PARKING
SET start_time = ?
WHERE id=?;

UPDATE PARKING
SET free_period = ?
WHERE id=?;

UPDATE PARKING
SET payment_per_hour = ?
WHERE id=?

UPDATE PARKING
SET stage_id = ?
WHERE id=?;

UPDATE PARKING
SET cloased = 1
WHERE id=?;