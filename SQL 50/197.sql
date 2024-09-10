# Write your MySQL query statement below
SELECT w1.id FROM Weather w1, Weather W2 
WHERE DATEDIFF(w1.recordDate, W2.recordDate) = 1 and w1.temperature > W2.temperature