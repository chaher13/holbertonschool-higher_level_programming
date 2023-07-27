-- Script to create the database hbtn_0d_usa if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Script to select the database hbtn_0d_usa to create the table cities inside it.
USE hbtn_0d_usa;

-- Script to create the table cities in the database hbtn_0d_usa if it doesn't exist.
-- The table cities has three columns: id (INT) auto-generated, unique, not null, and is the primary key,
-- state_id (INT) not null, a foreign key that references the id column of the states table,
-- and name (VARCHAR(256)) not null.
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
