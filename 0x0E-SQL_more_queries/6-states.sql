-- Create the table states if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
  id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
  name VARCHAR(256) NOT NULL
);
