drop table if exists ORDERS;

create table ORDERS (
    ord_id varchar PRIMARY KEY,
    cust_id varchar,
    prod_id varchar,
    count smallint
);