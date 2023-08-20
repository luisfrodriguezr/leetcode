# Write your MySQL query statement below
SELECT employee_id, salary * (name not like 'M%') * (employee_id % 2) AS bonus
FROM Employees
ORDER BY employee_id