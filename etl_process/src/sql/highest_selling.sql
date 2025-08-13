SELECT
        f.title,
        COUNT(*)
    FROM
        film as f
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
        f.title
    ORDER BY 
        COUNT(p.amount) DESC