/*
Con el resultado anterior visualizado previamente, escribe una consulta que extraiga los identificadores de vuelo que han volado con un Boeing 737. (Código Modelo Avión = 733)
*/
SELECT *
FROM aircrafts_data
WHERE aircraft_code = '733';