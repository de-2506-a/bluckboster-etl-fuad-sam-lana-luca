-- Top 5 categories by average price
SELECT 
    c.name AS category,
    AVG(p.amount) AS avg_price,
    SUM(p.amount) AS total_revenue,
    COUNT(p.payment_id) AS num_payments,
    'Top 5' AS group_label
FROM 
    main.payment p
JOIN main.rental r ON p.rental_id = r.rental_id
JOIN main.inventory i ON r.inventory_id = i.inventory_id
JOIN main.film f ON i.film_id = f.film_id
JOIN main.film_category fc ON f.film_id = fc.film_id
JOIN main.category c ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY avg_price DESC
LIMIT 5

UNION ALL

-- Bottom 5 categories by average price
SELECT 
    c.name AS category,
    AVG(p.amount) AS avg_price,
    SUM(p.amount) AS total_revenue,
    COUNT(p.payment_id) AS num_payments,
    'Bottom 5' AS group_label
FROM 
    main.payment p
JOIN main.rental r ON p.rental_id = r.rental_id
JOIN main.inventory i ON r.inventory_id = i.inventory_id
JOIN main.film f ON i.film_id = f.film_id
JOIN main.film_category fc ON f.film_id = fc.film_id
JOIN main.category c ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY avg_price ASC
LIMIT 5;
