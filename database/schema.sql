
CREATE TABLE animals (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
species TEXT NOT NULL, 
birth_date TEXT, 
weight REAL CHECK(weight>0)
);

CREATE TABLE vaccinesapplication (
id INTEGER PRIMARY KEY AUTOINCREMENT,
animal_id INTEGER NOT NULL,
vaccine_name TEXT NOT NULL,
apply_date TEXT NOT NULL,

FOREIGN KEY (animal_id) 
    REFERENCES animals(id)
);

CREATE TABLE feedingrecord (
id INTEGER PRIMARY KEY AUTOINCREMENT,
animal_id INTEGER NOT NULL,
type_feeding TEXT NOT NULL,
quantity_feeding REAL NOT NULL,
date_feeding TEXT NOT NULL,

FOREIGN KEY (animal_id)
    REFERENCES animals(id)
);

CREATE TABLE milkproductionrecord (
id INTEGER PRIMARY KEY AUTOINCREMENT,
animal_id INTEGER NOT NULL,
quantity_production NUMBER NOT NULL,
production_date TEXT NOT NULL,

FOREIGN KEY (animal_id)
    REFERENCES animals(id)
)