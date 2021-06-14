SELECT SUM(AMOUNT),COUNT(CHECKNUMBER) FROM CLASSICMODELS.PAYMENTS;

use classicmodels;
Select customerNumber, country from Customers where country not in('USA', 'UK');

Select count(customerNumber) from Customers where country IS NULL;

select *
from customers
left join orders
on customers.customerNumber = orders.customernumber;

select email from employees
where jobtitle = 'Sales Rep';

select distinct officecode from employees;

select * from employees;

select distinct productcode,productname from products where buyprice >= 70;

select ordernumber, priceeach from orderdetails where priceeach >= '100';