SELECT player_id, event_date AS first_login
FROM Activity e
WHERE event_date = (
    SELECT MIN(a.event_date)
    FROM Activity a
    WHERE a.player_id = e.player_id
);
