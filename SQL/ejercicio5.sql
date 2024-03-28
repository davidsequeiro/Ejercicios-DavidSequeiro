/*Ejercicio 5
1. Crea una tabla llamada "Clientes" con las columnas id (entero) y nombre
(cadena de texto).*/
CREATE TABLE Clientes(
id SERIAL PRIMARY KEY,
nombre VARCHAR(255)
	)

/*2. Inserta un cliente con id=1 y nombre='John' en la tabla "Clientes".*/
INSERT INTO Clientes(nombre)
VALUES ('John')

/*3. Actualiza el nombre del cliente con id=1 a 'John Doe' en la tabla "Clientes".*/
UPDATE Clientes
SET nombre = 'John Doe'
WHERE id = 1

/*4. Elimina el cliente con id=1 de la tabla "Clientes".*/
DELETE FROM clientes
WHERE id = 1

/*5. Lee todos los clientes de la tabla "Clientes".*/
SELECT * FROM clientes

/*6. Crea una tabla llamada "Pedidos" con las columnas id (entero) y cliente_id
(entero).*/
CREATE TABLE Pedidos(
id SERIAL PRIMARY KEY,
cliente_id INT,
FOREIGN KEY (cliente_id) REFERENCES clientes (id)
)

/*7. Inserta un pedido con id=1 y cliente_id=1 en la tabla "Pedidos".*/
-- al eliminar los registros en clientes me da error,creo un registro nuevo en clientes 
INSERT INTO Clientes(id,nombre)
VALUES (1,'John')

INSERT INTO pedidos (cliente_id) --introduzco registro en pedidos
VALUES(1)


/*8. Actualiza el cliente_id del pedido con id=1 a 2 en la tabla "Pedidos".*/
UPDATE pedidos
SET cliente_id = 2
WHERE id = 1

/*9. Elimina el pedido con id=1 de la tabla "Pedidos".*/
DELETE FROM pedidos
WHERE id = 1

/*10. Lee todos los pedidos de la tabla "Pedidos".*/
SELECT* FROM pedidos

/*11. Crea una tabla llamada "Productos" con las columnas id (entero) y nombre
(cadena de texto).*/
CREATE TABLE Productos(
id INT PRIMARY KEY,
nombre VARCHAR(255)
)

/*12. Inserta un producto con id=1 y nombre='Camisa' en la tabla "Productos".*/
INSERT INTO productos(id,nombre)
VALUES (1,'Camisa')

/*13. Actualiza el nombre del producto con id=1 a 'Pantalón' en la tabla "Productos".*/
UPDATE productos
SET nombre = 'Pantalon'
WHERE id = 1

/*14. Elimina el producto con id=1 de la tabla "Productos".*/
DELETE FROM productos
WHERE ID = 1

/*15. Lee todos los productos de la tabla "Productos".*/
SELECT* FROM productos

/*16. Crea una tabla llamada "DetallesPedido" con las columnas pedido_id (entero) y
producto_id (entero).*/
CREATE TABLE DetallesPedido(
id SERIAL PRIMARY KEY,
	pedido_id INT,
	producto_id INT,
	FOREIGN KEY (pedido_id) REFERENCES pedidos (id)
	FOREIGN KEY (producto_id) REFERENCES productos (id)
)

/*17. Inserta un detalle de pedido con pedido_id=1 y producto_id=1 en la tabla
"DetallesPedido".*/
INSERT INTO detallespedido(id,producto_id)
VALUES (1,1)

/*18. Actualiza el producto_id del detalle de pedido con pedido_id=1 a 2 en la tabla
"DetallesPedido".*/
UPDATE detallespedido
SET producto_id = 2
WHERE id = 1

/*19. Elimina el detalle de pedido con pedido_id=1 de la tabla "DetallesPedido".*/
DELETE FROM detallespedido
WHERE ID = 1

/*20. Lee todos los detalles de pedido de la tabla "DetallesPedido".*/
SELECT* FROM productos

/*21. Realiza una consulta para obtener todos los clientes y sus pedidos
correspondientes utilizando un inner join.*/
SELECT c.nombre AS clientes,
	   	 pe.id AS pedidos
FROM clientes c
INNER JOIN pedidos pe ON c.id = pe.cliente_id

/*22. Realiza una consulta para obtener todos los clientes y sus pedidos
correspondientes utilizando un left join.*/
SELECT c.nombre AS clientes,
	   pe.id AS pedidos
FROM clientes c
LEFT JOIN pedidos pe ON c.id = pe.cliente_id

--Forma optima para obtener nombres de clientes y nombre de productos comprados
SELECT c.nombre AS clientes,
	   po.nombre AS productos
FROM clientes c
LEFT JOIN pedidos pe ON c.id = pe.cliente_id
LEFT JOIN detallespedido dp ON pe.id = dp.pedido_id
LEFT JOIN productos po ON po.id = dp.producto_id

/*23. Realiza una consulta para obtener todos los productos y los detalles de pedido
correspondientes utilizando un inner join.*/
SELECT po.nombre AS nombre,
		dp.id AS pedido
FROM productos po 
INNER JOIN detallespedido dp ON po.id = dp.producto_id

/*24. Realiza una consulta para obtener todos los productos y los detalles de pedido
correspondientes utilizando un left join.*/
SELECT po.nombre AS nombre,
		dp.id AS pedido
FROM productos po 
LEFT JOIN detallespedido dp ON po.id = dp.producto_id

/*25. Crea una nueva columna llamada "telefono" de tipo cadena de texto en la tabla
"Clientes".*/
ALTER TABLE clientes
ADD COLUMN telefono VARCHAR(255)

/*26. Modifica la columna "telefono" en la tabla "Clientes" para cambiar su tipo de
datos a entero.*/
ALTER TABLE clientes
ALTER COLUMN telefono INT

/*27. Elimina la columna "telefono" de la tabla "Clientes".*/
ALTER TABLE clientes
DROP telefono

/*28. Cambia el nombre de la tabla "Clientes" a "Usuarios".*/
ALTER TABLE clientes
RENAME TO usuarios

/*29. Cambia el nombre de la columna "nombre" en la tabla "Usuarios" a
"nombre_completo".*/
ALTER TABLE usuarios
RENAME nombre TO nombre_completo

/*30. Agrega una restricción de clave primaria a la columna "id" en la tabla "Usuarios".
*/
--Crada reestricion al crear la tabla.