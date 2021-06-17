SELECT * FROM Fashion.women_clothing;

select `Division Name`, avg(Rating) avg_Rate
from fashion.women_clothing
group 
by 1 
order by 2 desc;

