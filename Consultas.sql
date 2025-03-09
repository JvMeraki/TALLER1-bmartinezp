-- Query para insertar datos a tabla GUARDERIAS 
INSERT INTO `GUARDERIAS` (`ID`, `Nombre`, `Direccion`, `Telefono`) VALUES
(1, 'Guarderia Sol', 'Avenida Libertad 123', '555-1234567'),
(2, 'Guarderia Luna', 'Calle 456', '555-2345678'),
(3, 'Guarderia Estrella', 'Calle del Sol 789', '555-3456789'),
(4, 'Guarderia Arco Iris', 'Avenida Central 101', '555-4567890'),
(5, 'Guarderia Pinos', 'Calle 34', '555-5678901'),
(6, 'Guarderia Felina', 'Carretera del Norte 233', '555-6789012'),
(7, 'Guarderia Canina', 'Plaza Mayor 12', '555-7890123'),
(8, 'Guarderia Infantil', 'Calle Fina 25', '555-8901234'),
(9, 'Guarderia Jardin de Mascotas', 'Avenida Primavera 567', '555-9012345'),
(10, 'Guarderia Patitas', 'Calle de la Alegria 87', '555-0123456'),
(11, 'La Favorita', 'Calle Falsa 123', '555- 2175345');
-- Query para consultar datos insertados
SELECT * FROM guarderias;

-- Query para insertar datos a tabla CUIDADOR
INSERT INTO `cuidador` (`ID`, `Nombre`, `Telefono`, `ID_GUARDERIA`) VALUES
(1, 'Juan Perez', '555-1112233', 1),
(2, 'Ana Gomez', '555-2223344', 2),
(3, 'Pedro Rodriguez', '555-3334455', 3),
(4, 'Lucia Martinez', '555-4445566', 4),
(5, 'Maria Lopez', '555-5556677', 5),
(6, 'Antonio Ruiz', '555-6667788', 6),
(7, 'Sofia Diaz', '555-7778899', 7),
(8, 'Raul Garcia', '555-8889900', 8),
(9, 'Carlos Fernandez', '555-9990011', 9),
(10, 'Elena Sanchez', '555-1011122', 10),
(11, 'Alba Navarro', '555-2122233', 1),
(12, 'David Torres', '555-3233344', 2),
(13, 'Ines Lopez', '555-4344455', 3),
(14, 'Jose Gomez', '555-5455566', 4),
(15, 'Patricia Jimenez', '555-6566677', 5),
(16, 'Mario', '555-1231236', 11);
-- Query para consultar datos insertados
SELECT * FROM cuidador;

-- QUERY Para insertar datos a tabla PERRO
INSERT INTO `PERRO` (`ID`, `Nombre`, `Raza`, `Edad`, `ID_GUARDERIA`, `ID_CUIDADOR`) VALUES
(1, 'Rex', 'Labrador', 5, 1, 1),
(2, 'Bella', 'Poodle', 3, 1, 1),
(3, 'Max', 'Beagle', 4, 2, 2),
(4, 'Rocky', 'Bulldog', 2, 2, 2),
(5, 'Fido', 'Chihuahua', 6, 3, 3),
(6, 'Charlie', 'Golden Retriever', 1, 3, 3),
(7, 'Luna', 'Pastor Aleman', 4, 4, 4),
(8, 'Leo', 'Boxer', 3, 4, 4),
(9, 'Milo', 'Dachshund', 2, 5, 5),
(10, 'Chester', 'Pug', 5, 5, 5),
(11, 'Buddy', 'Rottweiler', 6, 6, 6),
(12, 'Shadow', 'Schnauzer', 3, 6, 6),
(13, 'Daisy', 'Poodle', 1, 7, 7),
(14, 'Zoe', 'Cocker Spaniel', 2, 7, 7),
(15, 'Felix', 'Beagle', 5, 8, 8),
(16, 'Rocky', 'Labrador', 4, 8, 8),
(17, 'Oscar', 'Shih Tzu', 3, 9, 9),
(18, 'Bella', 'Pastor Aleman', 6, 9, 9),
(19, 'Rex', 'Golden Retriever', 4, 10, 10),
(20, 'Molly', 'Chihuahua', 3, 10, 10),
(21, 'Bobby', 'Jack Russell', 2, 1, 11),
(22, 'Ruby', 'Boxer', 1, 2, 12),
(23, 'Maximus', 'Pitbull', 5, 3, 13),
(24, 'Bella', 'Shih Tzu', 2, 4, 14),
(25, 'Charlie', 'Beagle', 4, 5, 15),
(26, 'Lucy', 'Labrador', 6, 6, 6),
(27, 'Buster', 'Collie', 2, 7, 7),
(28, 'Rosie', 'Poodle', 3, 8, 8),
(29, 'Lucky', 'Bulldog', 5, 9, 9),
(30, 'Cooper', 'Golden Retriever', 2, 10, 10),
(31, 'Sasha', 'Border Collie', 3, 2, 12),
(32, 'Duke', 'Labrador', 4, 3, 13),
(33, 'Simba', 'Dálmata', 2, 4, 14),
(34, 'Nina', 'Husky', 5, 5, 15),
(35, 'Rocko', 'Pastor Belga', 3, 6, 6),
(36, 'Rufus', 'Pug', 2, 7, 7),
(37, 'Maggie', 'Shih Tzu', 1, 8, 8),
(38, 'Chico', 'Chihuahua', 6, 9, 9),
(39, 'Lola', 'Bulldog Francés', 4, 10, 10),
(40, 'Bolt', 'Golden Retriever', 3, 1, 11),
(41, 'Coco', 'Caniche', 2, 2, 12),
(42, 'Max', 'Dálmata', 5, 3, 13),
(43, 'Bobby', 'Pastor Alemán', 4, 4, 14),
(44, 'Milo', 'Beagle', 3, 5, 15),
(45, 'Luna', 'Golden Retriever', 2, 6, 6),
(46, 'Zeus', 'Doberman', 6, 7, 7),
(47, 'Rocky', 'Bulldog Inglés', 4, 8, 8),
(48, 'Toby', 'Pug', 3, 9, 9),
(49, 'Rex', 'Labrador', 5, 10, 10),
(50, 'Bella', 'Cocker Spaniel', 4, 1, 11),
(51, 'Lucky', 'Boxer', 2, 2, 12),
(52, 'Simon', 'Jack Russell', 3, 3, 13),
(53, 'Daisy', 'Poodle', 1, 4, 14),
(54, 'Tommy', 'Rottweiler', 6, 5, 15),
(55, 'Lenny', 'Husky Siberiano', 5, 6, 6),
(56, 'Oreo', 'Shih Tzu', 2, 7, 7),
(57, 'Bruno', 'Dogo Argentino', 4, 8, 8),
(58, 'Charlie', 'Pastor Belga', 3, 9, 9),
(59, 'Lily', 'Bulldog Francés', 1, 10, 10),
(60, 'Simba', 'Golden Retriever', 5, 1, 11);
-- Query para consultar datos insertados
SELECT * FROM PERRO;


-- Taller
SELECT * FROM GUARDERIAS;
SELECT * FROM CUIDADOR WHERE ID = 16;
SELECT * FROm PERRO WHERE ID_CUIDADOR = 13;

-- Punto 1
SELECT * FROM PERRO WHERE Nombre = 'Lassie';


SET SQL_SAFE_UPDATES = 0;

-- Punto 2
UPDATE PERRO 
SET ID_CUIDADOR = 16
WHERE Peso < 3 AND ID_GUARDERIA = 11;

SELECT * FROm PERRO WHERE Peso < 3 AND ID_GUARDERIA = 11;


SELECT * FROM GUARDERIAS WHERE Nombre = 'La Favorita';
SELECT * FROM CUIDADOR WHERE ID_GUARDERIA = 11;
SELECT * FROM PERRO WHERE ID_GUARDERIA = 11;

