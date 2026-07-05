# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1
JOIN Weather w2
ON DATEDIFF(w1.recordDate , w2.recordDate) = 1
WHERE w1.temperature > w2.temperature

-- pairder like this 

-- w1           w2

-- Jan2   <-->  Jan1
-- Jan3   <-->  Jan2
-- Jan4   <-->  Jan3