--  script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(temp_fahrenheit) AS avg_temp FROM weather_data GROUP BY city ORDER BY avg_temp DESC;
