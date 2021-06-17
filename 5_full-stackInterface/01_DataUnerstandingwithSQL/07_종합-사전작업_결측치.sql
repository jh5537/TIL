use TIP_Schema;

select * from tips; 

insert into tips(total_bill, tip, sex, smoker, day, time, size)
values(16.99, null, 'Female', 'No', 'Sun', 'Dinner', 2);

insert into tips(total_bill, tip, sex, smoker, day, time, size)
values(20.34, 1.66, null, 'No', 'Sun', 'Dinner', 3);

insert into tips(total_bill, tip, sex, smoker, day, time, size)
values(13.23, 2.66, 'Male', 'Yes', 'Sat', null, null);

insert into tips(total_bill, tip, sex, smoker, day, time, size)
values(26.34, 2.2, 'Female', 'No', 'Fri', 'Lunch', 4);

select * from tips;

# -- 삭제
select * from tips where tips.sex is null;
select * from tips where tips.tip is null;

delete from tips where tips.sex is null;
delete from tips where tips.tip is null;

select * from tips;