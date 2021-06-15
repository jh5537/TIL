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

show tables;

select * from employees;

select firstName, lastname, employeenumber from employees where employees.employeenumber >= 1300;

select customers.customernumber, orders.ordernumber, customers.country from orders
left join customers 
on orders.customernumber = customers.customernumber;

select orders.ordernumber, customers.country from orders
inner join customers on orders.customernumber = customers.customernumber
where customers.country = 'USA';

select customers.customername, payments.checknumber from classicmodels.customers
left join payments on customers.customernumber=payments.customernumber where payments.paymentdate >= '2004-06-06';