CREATE DATABASE cafe;
USE cafe;

CREATE TABLE menu(
    item VARCHAR(30),
    price FLOAT
);

INSERT INTO menu VALUES
('Coffee', 2.50),
('Tea', 2.00),
('Sandwich', 5.00),
('Cake', 3.00),
('Juice', 3.50);

CREATE TABLE orders(
    item VARCHAR(30),
    price FLOAT
);


