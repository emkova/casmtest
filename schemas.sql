DROP TABLE IF EXISTS prompts;

CREATE TABLE prompts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  reflection TEXT NOT NULL,
  msg TEXT NOT NULL
);