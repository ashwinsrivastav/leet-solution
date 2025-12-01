1# Write your MySQL query statement below
2SELECT
3    w1.id
4FROM
5    Weather w1
6JOIN
7    Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
8WHERE
9    w1.temperature > w2.temperature;
10