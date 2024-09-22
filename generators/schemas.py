CUSTOMERS_SCHEMA = [{
    "name": "cust_id",
    "type": 'id'
}, {
    "name": "name",
    "type": 'cust_name'
}, {
    "name": "sex",
    "type": "sex"
}, {
    "name": "age",
    "type": "age"
}, {
    "name": "address",
    "type": "address"
}, {
    "name": "phone",
    "type": "phone"
}, {
    "name": "job",
    "type": "job"
}]

PRODUCTS_SCHEMA = [{
    "name": "prod_id",
    "type": "id"
}, {
    "name": "name",
    "type": "prod_name"
}, {
    "name": "price",
    "type": "price"
}]

ORDERS_SCHEMA = [{
    "name": "ord_id",
    "type": "id"
}, {
    "name": "cust_id",
    "type": "id"
}, {
    "name": "prod_id",
    "type": "id"
}, {
    "name": "quantity",
    "type": "quantity"
}]