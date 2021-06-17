use TIP_Schema;

select * from tips;

select total_bill from TIP_Schema.tips where tip >= 7;

SELECT total_bill, tip, smoker, time
FROM tips
LIMIT 5;

select day, avg(tip), count(*)
from tips
group by day;

select day, avg(tip), count(*)
from tips
group by day order by day asc;

select day, avg(tip), count(*)
from tips
group by day order by day desc;

select smoker, avg(tip), count(*)
from TIP_Schema.tips
group by smoker, day order by smoker;