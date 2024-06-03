USE sakila;

# 1: Next, you need to analyze the films in the collection to gain some more insights. Using the film table, determine:
# 1.1 The total number of films that have been released.
SELECT COUNT(*) FROM film;

# 1.2 The number of films for each rating.
SELECT COUNT(*), rating
FROM film
GROUP BY rating;

# 1.3 The number of films for each rating, sorting the results in descending order of the number of films. 
# This will help you to better understand the popularity of different film ratings and adjust purchasing decisions accordingly.
SELECT COUNT(*), rating
FROM film
GROUP BY rating
ORDER BY rating DESC;

# 2: Using the film table, determine:
# 2.1 The mean film duration for each rating, and sort the results in descending order of the mean duration.
# Round off the average lengths to two decimal places. 
# This will help identify popular movie lengths for each category.
SELECT rating, ROUND(AVG(length),2) AS mean_duration
FROM film
GROUP BY rating
ORDER BY mean_duration DESC;

# 2.2 Identify which ratings have a mean duration of over two hours in order to help select films for
# customers who prefer longer movies.
SELECT rating AS rating_duration_over_2_hours
FROM film
GROUP BY rating
HAVING ROUND(AVG(length),2) > 120;

# 3 Bonus: determine which last names are not repeated in the table actor.
# this would retrieve  the unique last names, with no regard of it being repeated (no count)
# SELECT DISTINCT(last_name) FROM actor;

# group by last_name, I can then count the groups 
SELECT last_name 
FROM actor
GROUP BY last_name
HAVING count(*) = 1;