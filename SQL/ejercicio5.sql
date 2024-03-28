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


/*7. Inserta un pedido con id=1 y cliente_id=1 en la tabla "Pedidos".*/


/*8. Actualiza el cliente_id del pedido con id=1 a 2 en la tabla "Pedidos".*/


/*9. Elimina el pedido con id=1 de la tabla "Pedidos".*/


/*10. Lee todos los pedidos de la tabla "Pedidos".*/


/*11. Crea una tabla llamada "Productos" con las columnas id (entero) y nombre
(cadena de texto).*/


/*12. Inserta un producto con id=1 y nombre='Camisa' en la tabla "Productos".*/


/*13. Actualiza el nombre del producto con id=1 a 'Pantalón' en la tabla "Productos".*/


/*14. Elimina el producto con id=1 de la tabla "Productos".*/


/*15. Lee todos los productos de la tabla "Productos".*/


/*16. Crea una tabla llamada "DetallesPedido" con las columnas pedido_id (entero) y
producto_id (entero).*/


/*17. Inserta un detalle de pedido con pedido_id=1 y producto_id=1 en la tabla
"DetallesPedido".*/


/*18. Actualiza el producto_id del detalle de pedido con pedido_id=1 a 2 en la tabla
"DetallesPedido".*/


/*19. Elimina el detalle de pedido con pedido_id=1 de la tabla "DetallesPedido".*/


/*20. Lee todos los detalles de pedido de la tabla "DetallesPedido".*/


/*21. Realiza una consulta para obtener todos los clientes y sus pedidos
correspondientes utilizando un inner join.*/


/*22. Realiza una consulta para obtener todos los clientes y sus pedidos
correspondientes utilizando un left join.*/


/*23. Realiza una consulta para obtener todos los productos y los detalles de pedido
correspondientes utilizando un inner join.*/


/*24. Realiza una consulta para obtener todos los productos y los detalles de pedido
correspondientes utilizando un left join.*/


/*25. Crea una nueva columna llamada "telefono" de tipo cadena de texto en la tabla
"Clientes".*/


/*26. Modifica la columna "telefono" en la tabla "Clientes" para cambiar su tipo de
datos a entero.*/


/*27. Elimina la columna "telefono" de la tabla "Clientes".*/


/*28. Cambia el nombre de la tabla "Clientes" a "Usuarios".*/


/*29. Cambia el nombre de la columna "nombre" en la tabla "Usuarios" a
"nombre_completo".*/


/*30. Agrega una restricción de clave primaria a la columna "id" en la tabla "Usuarios".
*/