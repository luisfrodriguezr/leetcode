# Write your MySQL query statement below
SELECT tweet_id
FROM Tweets as T
WHERE LENGTH(T.content) > 15