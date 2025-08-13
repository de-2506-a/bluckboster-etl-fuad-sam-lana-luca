SELECT
    a.first_name,
    a.last_name,
    f.title,
    SUM(p.amount) as total_revenue
FROM
    film as f
INNER JOIN 
    film_actor as fa
ON
    f.film_id = fa.film_id
INNER JOIN 
    actor as a
ON
    fa.actor_id = a.actor_id
INNER JOIN 
    inventory as i
ON
    f.film_id = i.film_id
INNER JOIN 
    rental as r
ON
    i.inventory_id = r.inventory_id
INNER JOIN 
    payment as p
ON
    r.rental_id = p.rental_id
GROUP BY
    a.first_name, a.last_name, f.title
ORDER BY 
    total_revenue DESC