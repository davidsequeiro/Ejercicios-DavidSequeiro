/*Ejercicio 2
Nivel de dificultad: Fácil
1. Crea una base de datos llamada "MiBaseDeDatos".*/
CREATE database MiBaseDeDatos

/*2. Crea una tabla llamada "Usuarios" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "edad" (entero).*/
CREATE TABLE usuarios(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(255),
	edad INT
	)

/*3. Inserta dos registros en la tabla "Usuarios".*/
INSERT INTO usuarios (nombre,edad)
VALUES ('Juan',30),('Maria',32)

/*4. Actualiza la edad de un usuario en la tabla "Usuarios".*/
UPDATE usuarios
SET edad = 28
WHERE id = 1

/*5. Elimina un usuario de la tabla "Usuarios".*/
DELETE FROM usuarios
WHERE id = 1

/*Nivel de dificultad: Moderado
1. Crea una tabla llamada "Ciudades" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "pais" (texto).*/
CREATE TABLE Ciudades (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(255),
	pais VARCHAR(255)
)

/*2. Inserta al menos tres registros en la tabla "Ciudades".*/
INSERT INTO ciudades(nombre,pais)
VALUES ('Madrid','España'),
	   ('Paris','Francia'),
	   ('New York','EEUU')

/*3. Crea una foreign key en la tabla "Usuarios" que se relacione con la columna "id"
de la tabla "Ciudades".*/
ALTER TABLE usuarios --Creamos la tabla
ADD COLUMN Ciudades_id INT

ALTER TABLE usuarios --Alteramos la propiedad de la columna
ADD FOREIGN KEY (Ciudades_id) REFERENCES Ciudades (id)

/*4. Realiza una consulta que muestre los nombres de los usuarios junto con el
nombre de su ciudad y país (utiliza un LEFT JOIN).*/
SELECT usuarios.nombre, ciudades.nombre,ciudades.pais
FROM usuarios
LEFT JOIN ciudades
ON usuarios.ciudades_id = ciudades.id

/*5. Realiza una consulta que muestre solo los usuarios que tienen una ciudad
asociada (utiliza un INNER JOIN).*/
SELECT usuarios.nombre, ciudades.nombre,ciudades.pais
FROM usuarios
INNER JOIN ciudades
ON usuarios.ciudades_id = ciudades.id