-- Script to create the database hbtn_0d_usa if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Script to select the database hbtn_0d_usa to create the table states inside it.
USE hbtn_0d_usa;

-- Script to create the table states in the database hbtn_0d_usa if it doesn't exist.
-- The table states has two columns: id (INT) auto-generated, unique, not null, and is the primary key,
-- and name (VARCHAR(256)) not null.
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
