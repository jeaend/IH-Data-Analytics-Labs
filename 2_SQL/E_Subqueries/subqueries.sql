USE sakila;

# Write SQL queries to perform the following tasks using the Sakila database:

# 1: Determine the number of copies of the film "Hunchback Impossible" that exist in the inventory system.
SELECT COUNT(*) AS number_of_copies
FROM inventory
JOIN film
USING (film_id)
WHERE film.title = "Hunchback Impossible";

# 2: List all films whose length is longer than the average length of all the films in the Sakila database.
-- sounds like subquery, we need to get the avg length first 

# SELECT AVG(length) 
# FROM film;

SELECT title AS film_over_average_length
FROM film 
WHERE film.length > (
	SELECT AVG(length) 
	FROM film
);

# 3: Use a subquery to display all actors who appear in the film "Alone Trip".
-- subquery to retrieve id's from actors that are in the movie

SELECT actor.actor_id, CONCAT(first_name, ' ', last_name) AS Alone_Trip_Actor
FROM actor
WHERE actor.actor_id IN (
    SELECT actor_id
    FROM film
    JOIN film_actor 
    USING (film_id)
    WHERE film.title = 'Alone Trip'
);


# Bonus:

# 4: Sales have been lagging among young families, and you want to target family movies for a promotion. 
# Identify all movies categorized as family films.
-- subquery: select film_id where the id that maps to family movie

#SELECT fc.film_id
#    FROM film_category fc
#    JOIN category c ON fc.category_id = c.category_id
#    WHERE c.name = 'Family';
    
SELECT f.title, f.film_id
FROM film f
WHERE f.film_id IN (
    SELECT fc.film_id
    FROM film_category fc
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Family'
);

# 5: Retrieve the name and email of customers from Canada using both subqueries and joins.
# To use joins, you will need to identify the relevant tables and their primary and foreign keys.
# country > city > address > customer

SELECT CONCAT(c.first_name, ' ', c.last_name) AS Name, c.email
FROM customer c
WHERE c.address_id IN (
    SELECT a.address_id
    FROM address a
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
    WHERE co.country = 'Canada'
);

# 6: Determine which films were starred by the most prolific actor in the Sakila database.
# A prolific actor is defined as the actor who has acted in the most number of films.
# First, you will need to find the most prolific actor and then use that actor_id to find the different films that he or she starred in.

# MOST PROLIFIC ACTOR (ID)
SELECT actor_id
FROM (
    SELECT actor_id
    FROM film_actor
    GROUP BY actor_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
) AS most_prolific_actor;

# use that actor_id to find the different films that he or she starred in.
SELECT f.title
FROM film f
JOIN film_actor fa USING(film_id)
WHERE fa.actor_id = (
	SELECT actor_id
	FROM (
		SELECT actor_id
		FROM film_actor
		GROUP BY actor_id
		ORDER BY COUNT(*) DESC
		LIMIT 1
	) AS most_prolific_actor
);

# 7: Find the films rented by the most profitable customer in the Sakila database.
# You can use the customer and payment tables to find the most profitable customer,
# i.e., the customer who has made the largest sum of payments.


# 8: Retrieve the client_id and the total_amount_spent of those clients who spent more than the average
# of the total_amount spent by each client. You can use subqueries to accomplish this.