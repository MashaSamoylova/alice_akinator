SELECT place, start_time, free_period, payment_per_hour from PARKING
WHERE session_id=? AND user_id=?;

SELECT id, user_id, session_id, place, start_time, free_period, payment_per_hour, stage_id, closed from PARKING
WHERE  id = (SELECT MAX(id) FROM PARKING WHERE session_id=? AND user_id=? and closed=0);