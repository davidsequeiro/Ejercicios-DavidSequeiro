/*
Escribe una consulta que extraiga todas las columnas de la tabla bookings y refleje todas las reservas que han supuesto una cantidad totSELECTal mayor a 1.000.000 (Unidades monetarias).
*/
SELECT *
FROM bookings
WHERE total_amount > 1000000;