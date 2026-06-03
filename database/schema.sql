
CREATE TABLE animals (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
especie TEXT NOT NULL, 
birth_date TEXT, 
weight REAL CHECK(weight>0)
);

SELECT * FROM animals;