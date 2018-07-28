create table PARKING (
  user_id TEXT not null ,
  session_id TEXT not null,
  place TEXT,
  start_time TEXT,
  free_period INTEGER,
  payment_per_hour INTEGER
);