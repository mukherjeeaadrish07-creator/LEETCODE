# Write your MySQL query statement below
Select u.name as NAME , sum(t.amount) as BALANCE
from Users u join Transactions t
on u.account = t.account
group by u.account
having sum(t.amount) > 10000
