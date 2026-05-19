-- Comandos DDL - Criando o BD e as tabelas iniciais

CREATE TABLE animals (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL,
species VARCHAR(50) NOT NULL,
birth_date DATE,
weight NUMERIC(6,2) CHECK (weight > 0)
);

CREATE TABLE plantations (
id SERIAL PRIMARY KEY,
crop_type VARCHAR(50) NOT NULL,
planting_date DATE NOT NULL, 
expected_harvest_date DATE,
area_hectares NUMERIC(6,2),
status VARCHAR(30)
);

CREATE TABLE vaccines (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL,
manufacturer VARCHAR(50) NOT NULL,
expiration_date DATE
);

-- INSERINDO DADOS NAS TABELAS

INSERT INTO animals (name, species, birth_date, weight)
VALUES 
('Garanhão', 'horse', '2021-07-10', 120),
('Tourão', 'bull', '2025-03-12', 150),
('Giganta', 'cow', '2020-02-01', 200),
('Ferinha', 'bull', '2016-01-25', 120),
('Dolomito', 'horse', '2024-08-29', 120),
('Lindinha', 'cow', '2023-02-26', 95);

INSERT INTO plantations (crop_type, planting_date, area_hectares)
VALUES 
('Coin', '2026-03-29', 50),
('Soya', '2026-04-01', 60),
('Cana', '2026-01-23', 20);

INSERT INTO vaccines (name, manufacturer, expiration_date) 
VALUES
('Antirábica', 'Pfizer', '2026-11-01'),
('Febre aftosa', 'Jhonsons', '2026-10-02'),
('Vaca Louca', 'Astrazenica', '2026-10-01');

UPDATE plantations
SET crop_type = 'corn'
WHERE id = 1;

UPDATE plantations
SET crop_type = 'soybean'
WHERE id = 2;

UPDATE plantations
SET crop_type = 'Sugarcane'
WHERE id = 3;

SELECT * FROM plantations;