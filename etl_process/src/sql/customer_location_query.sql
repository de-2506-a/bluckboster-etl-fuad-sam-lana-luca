SELECT 
                COUNT(customer.customer_id) AS total_customers, 
                city.city, 
                country.country
            FROM 
                customer
            LEFT JOIN 
                address
            ON 
                customer.address_id = address.address_id
            LEFT JOIN
                city
            ON
                address.city_id = city.city_id
            LEFT JOIN
                country
            ON
                city.country_id = country.country_id
            GROUP BY
                city.city, country.country
            ORDER BY
                total_customers DESC
            ;