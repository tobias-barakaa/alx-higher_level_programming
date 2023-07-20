-- script that Creates a unique Id 
CREATE TABLE IF NOT EXISTS unique_id(
     id INT DEFAULT 1 UNIQUE,
     name VARCHAR(256)
);
