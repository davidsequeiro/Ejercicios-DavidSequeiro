/*
Escribe una consulta que recupere los Vuelos (flights) y su identificador que figuren con status On Time.
*/
SELECT flight_id,flight_no
FROM flights
WHERE status = 'On Time';