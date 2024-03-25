/* ## Ejercicio 1 
1. Crear una tabla llamada "Clientes" con las columnas: id (entero, clave primaria), nombre (texto) y email (texto). 
2. Insertar un nuevo cliente en la tabla "Clientes" con id=1, nombre="Juan" y email=" juan@example.com". 
3. Actualizar el email del cliente con id=1 a " juan@gmail.com". 
4. Eliminar el cliente con id=1 de la tabla "Clientes". 
5. Crear una tabla llamada "Pedidos" con las columnas: id (entero, clave primaria), cliente_id (entero, clave externa referenciando a la tabla "Clientes"), producto (texto) y cantidad (entero). 
6. Insertar un nuevo pedido en la tabla "Pedidos" con id=1, cliente_id=1, producto="Camiseta" y cantidad=2. 
7. Actualizar la cantidad del pedido con id=1 a 3. 
8. Eliminar el pedido con id=1 de la tabla "Pedidos". 
9. Crear una tabla llamada "Productos" con las columnas: id (entero, clave primaria), nombre (texto) y precio (decimal). 
10. Insertar varios productos en la tabla "Productos" con diferentes valores. 
11. Consultar todos los clientes de la tabla "Clientes". 
12. Consultar todos los pedidos de la tabla "Pedidos" junto con los nombres de los clientes correspondientes. 
13. Consultar los productos de la tabla "Productos" cuyo precio sea mayor a $50. 
14. Consultar los pedidos de la tabla "Pedidos" que tengan una cantidad mayor o igual a 5. 
15. Consultar los clientes de la tabla "Clientes" cuyo nombre empiece con la letra "A".
16. Realizar una consulta que muestre el nombre del cliente y el total de pedidos realizados por cada cliente. 
17. Realizar una consulta que muestre el nombre del producto y la cantidad total de pedidos de ese producto. 
18. Agregar una columna llamada "fecha" a la tabla "Pedidos" de tipo fecha. 
19. Agregar una clave externa a la tabla "Pedidos" que haga referencia a la tabla "Productos" en la columna "producto". 
20. Realizar una consulta que muestre los nombres de los clientes, los nombres de los productos y las cantidades de los pedidos donde coincida la clave externa.