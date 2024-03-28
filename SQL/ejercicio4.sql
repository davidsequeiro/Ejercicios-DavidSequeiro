/*
Ejercicio 4
Nivel de dificultad: Experto
1. Crea una tabla llamada "Pedidos" con las columnas: "id" (entero, clave
primaria), "id_usuario" (entero, clave foránea de la tabla "Usuarios") y
"id_producto" (entero, clave foránea de la tabla "Productos").*/
CREATE TABLE pedidos(
	id SERIAL PRIMARY KEY,
	id_usuario INT,
	id_producto INT,
	FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
	FOREIGN KEY (id_producto) REFERENCES productos(id)
)


/*2. Inserta al menos tres registros en la tabla "Pedidos" que relacionen usuarios con
productos.*/
INSERT INTO pedidos (id_usuario,id_producto)
VALUES (2,4),(1,3),(3,2),(4,5)

/*3. Realiza una consulta que muestre los nombres de los usuarios y los nombres de
los productos que han comprado, incluidos aquellos que no han realizado
ningún pedido (utiliza LEFT JOIN y COALESCE).*/
SELECT
	u.nombre AS Usuario,
	COALESCE(p.nombre,'Sin compra') AS Producto
FROM usuarios u
LEFT JOIN pedidos pe ON u.id = pe.id_usuario
LEFT JOIN productos p ON pe.id_producto = p.id

/*4. Realiza una consulta que muestre los nombres de los usuarios que han
realizado un pedido, pero también los que no han realizado ningún pedido
(utiliza LEFT JOIN).*/
SELECT
	u.nombre AS Usuario,
	p.nombre AS Producto
FROM usuarios u
LEFT JOIN pedidos pe ON u.id = pe.id_usuario
LEFT JOIN productos p ON pe.id_producto = p.id

/*5. Agrega una nueva columna llamada "cantidad" a la tabla "Pedidos" y actualiza
los registros existentes con un valor (utiliza ALTER TABLE y UPDATE)*/
ALTER TABLE pedidos --agregamos la columna cantidad
ADD COLUMN cantidad INT;

UPDATE pedidos --Actulizamos valores de cantidad = 1
SET cantidad = 1

