create table PARKING (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  user_id TEXT not null ,
  session_id TEXT not null,
  place TEXT,
  start_time TEXT,
  free_period INTEGER,
  payment_per_hour INTEGER,
  stage_id TEXT,
  closed INTEGER
);

DROP table PARKING