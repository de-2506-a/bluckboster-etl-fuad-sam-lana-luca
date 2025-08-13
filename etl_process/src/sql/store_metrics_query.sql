SELECT
    s.store_id,
    SUM(p.amount) AS total_revenue
FROM
    main.payment p
JOIN
    main.staff s
ON
    p.staff_id = s.staff_id
JOIN
    main.store st
ON
    s.store_id = st.store_id
GROUP BY
    s.store_id
ORDER BY
    total_revenue DESC;