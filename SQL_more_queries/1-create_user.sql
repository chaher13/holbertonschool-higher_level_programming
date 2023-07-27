-- Script to create a MySQL server user named user_0d_1 with all privileges.
-- If the user user_0d_1 does not exist, it will be created, and the password will be set to user_0d_1_pwd.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
