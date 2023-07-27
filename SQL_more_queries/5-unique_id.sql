-- Script to create the table unique_id
-- The table unique_id has two columns: id (INT) with a default value of 1 and is marked as unique, and name (VARCHAR(256)).
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
