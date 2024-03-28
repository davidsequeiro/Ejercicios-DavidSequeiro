/*Ejercicio 3
Nivel de dificultad: Difícil

1. Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "precio" (numérico).*/

CREATE TABLE Productos (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(255),
	precio FLOAT
)

/*2. Inserta al menos cinco registros en la tabla "Productos".*/
INSERT INTO productos (nombre, precio)
VALUES ('Carne', 10),
	   ('Pescado', 12),
	   ('Huevos', 6),
	   ('Pan', 2),
	   ('Leche', 4),
     ('Patatas', 8)

/*3. Actualiza el precio de un producto en la tabla "Productos".*/
UPDATE productos
SET precio = 3
WHERE id = 5

/*4. Elimina un producto de la tabla "Productos".*/
DELETE productos
WHERE id = 6

/*5. Realiza una consulta que muestre los nombres de los usuarios junto con los
nombres de los productos que han comprado (utiliza un INNER JOIN con la
tabla "Productos").
*/

--Antes debemos crear la columna productos_id y referenciarla a productos(id)
ALTER TABLE usuarios
ADD COLUMN producto_id INT

ALTER TABLE usuarios
ADD FOREIGN KEY (producto_id) REFERENCES productos(id)

--Nos crea valores nulos por lo que debemos actualizar los valores
UPDATE usuarios
SET producto_id = 5 --modificamos este valor para el id de producto
WHERE id = 4 --modificamos este valor para el usuario

--Cruzamos datos
SELECT usuarios.nombre, productos.nombre
FROM usuarios
INNER JOIN productos
ON usuarios.producto_id = productos.id 
