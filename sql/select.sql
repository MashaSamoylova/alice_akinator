SELECT place, start_time, free_period, payment_per_hour from PARKING
WHERE session_id=? AND user_id=?;