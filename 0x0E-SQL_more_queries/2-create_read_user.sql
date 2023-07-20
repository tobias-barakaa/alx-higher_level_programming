-- Creates the database hbtn_0d_2 if it doesn't exist
  2 CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
  3 
  4 -- Create the user user_0d_2 if it doesn't exist and set the password
  5 CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
  6 
  7 -- Grant SELECT privilege on hbtn_0d_2 to the user user_0d_2
  8 GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
  9 
 10 -- Refresh the privileges
 11 FLUSH PRIVILEGES;
