drop table if exists CUSTOMER;

create table CUSTOMER (
    cust_id varchar PRIMARY KEY,
    name varchar,
    sex varchar,
    age decimal,
    address varchar,
    phone varchar,
    job varchar
);

-- insert into CUSTOMER(cust_id, name, sex, age, address, phone, job) VALUES('8A1e4231aDAdEe2','Mrs. Jean Meza','Male',27,'403 Dougherty Vista','3976292691','Scientist, forensic');
-- insert into CUSTOMER(cust_id, name, sex, age, address, phone, job) VALUES('CBc667D844E2ACD','Victoria Murray DVM','Female',61,'406 Goodman Greens','001-238-484-3687','Ship broker');
-- insert into CUSTOMER(cust_id, name, sex, age, address, phone, job) VALUES('EEeF1Afa85Baa60','Jody Huang DVM','Male',31,'2584 Bernard Flats Apt. 288','001-605-732-0463','Company secretary');
-- insert into CUSTOMER(cust_id, name, sex, age, address, phone, job) VALUES('9c73A8FC963E244','Miss Kimberly Ellison DVM','Male',38,'283 Albert Crescent','2808633631','Advice worker');
-- insert into CUSTOMER(cust_id, name, sex, age, address, phone, job) VALUES('b5f4f5D9f606Be4','Mrs. Ruth Macias','Female',45,'159 Cassandra Club','866-942-8076','Writer');
-- insert into CUSTOMER(cust_id, name, sex, age, address, phone, job) VALUES('b9405fF5aEDc7e6','Mr. Herbert Bray DDS','Male',39,'317 Ernest Well Apt. 041','(663)677-6900','Community arts worker');
-- insert into CUSTOMER(cust_id, name, sex, age, address, phone, job) VALUES('89552BdDE411a1B','Diamond Mcknight','Male',54,'853 Vincent Lodge Suite 664','9765050069','Tourism officer');
-- insert into CUSTOMER(cust_id, name, sex, age, address, phone, job) VALUES('7Bff74Ab9345B2B','Shaun Bonilla','Female',69,'759 Bolton Inlet Apt. 880','303-879-2297x90233','Interior and spatial designer');
-- insert into CUSTOMER(cust_id, name, sex, age, address, phone, job) VALUES('Fe7D64d3afBA406','Dr. Jermaine Espinoza V','Male',59,'251 Garrett Hills','(871)599-5544x262','Television/film/video producer');
-- insert into CUSTOMER(cust_id, name, sex, age, address, phone, job) VALUES('eB4Df05BcdAEB23','Henry GillespieIV','Male',64,'023 Ross Village','2332748174','Physiotherapist');
