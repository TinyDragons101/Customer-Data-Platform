drop table if exists SUM;

create table SUM (
    cust_id varchar PRIMARY KEY,
    count decimal,
    sum numeric(2)
);