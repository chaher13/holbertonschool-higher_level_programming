-- Script to create the table force_name in your MySQL server.
-- The table force_name has two columns: id (INT) and name (VARCHAR(256)) that cannot be null.
-- If the table force_name already exists, the script will not fail.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
