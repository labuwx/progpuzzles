SELECT DISTINCT ON (event_type) event_type, v1-v2
FROM (
    SELECT t1.event_type AS event_type,
           t1.value AS v1,
           t2.value AS v2
    FROM events AS t1 INNER JOIN
         events AS t2
    ON t1.event_type = t2.event_type AND
    t1.time > t2.time
    ORDER BY t1.event_type, t1.time DESC, t2.time DESC
) AS _
