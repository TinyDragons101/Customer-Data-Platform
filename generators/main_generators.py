import csv
from pathlib import Path
from zipfile import ZipFile, ZIP_BZIP2
import json
import pandas
import random

from generators import (
    TYPES_TO_GENERATORS,
    random_string
)

from schemas import (
    CUSTOMERS_SCHEMA,
    PRODUCTS_SCHEMA,
    ORDERS_SCHEMA
)

# def generate_file(schema='customers', name="customers-50", count=50):
#     p = Path(__file__).parent / "../datas"
#     p.mkdir(parents=True, exist_ok=True)

#     file_name = "{}.csv".format(name)
#     file_path = p / file_name

#     if file_path.exists():
#         schema_dict = SCHEMA_TO_DICT[schema]

#         with open(file_path, 'w', newline='') as file:
#             writer = csv.writer(file)

#             # Headers
#             headers = [elem['name'] for elem in schema_dict]
#             # headers.insert(0, "Index") # Add an Index header
#             writer.writerow(headers)

#             # Content
#             data_generators = [TYPES_TO_GENERATORS[elem['type']] for elem in schema_dict]

#             rows = []
#             for index in range(1, count+1):
#                 row = [gen() for gen in data_generators]
#                 # row.insert(0, index)
#                 rows.append(row)

#                 if index % 1000 == 0:
#                     writer.writerows(rows)
#                     rows = []

#                 if index % 10000 == 0:
#                     print("{}/{}".format(index, count))

#             writer.writerows(rows)
#     else:
#         print("{} already exists".format(file_path))

# def generate_product():
#     file_name = "products.csv"
#     file_path = Path(__file__).parent / "../datas" / file_name
    
#     if file_path.exists():
#         with open(file_path, 'w', newline='') as file:
#             writer = csv.writer(file)
            
#             # Headers
#             headers = [elem['name'] for elem in PRODUCTS_SCHEMA]
#             # headers.insert(0, "Index")
#             writer.writerow(headers)
#             rows = []
#             # Content
#             index = 1
#             for product in PRODUCTS:
#                 for size in range(1, 4):
#                     # row = [index]
#                     row = []
#                     row.append(TYPES_TO_GENERATORS['id']())
#                     row.append(product)
#                     row.append(size)
#                     row.append(TYPES_TO_GENERATORS['price']() * size)
#                     rows.append(row)
#                     index = index + 1
                
#             writer.writerows(rows)
#     else:
#         print("{} already exists".format(file_path))

# def generate_more_customers():
#     filepath = Path(__file__).parent / "../data/data/customers.csv"
#     schema_dict = CUSTOMERS_SCHEMA
#     rows = []
#     with open(filepath, 'a', newline='') as file:
#         writer = csv.writer(file)
#         data_generators = [TYPES_TO_GENERATORS[elem['type']] for elem in schema_dict]
        
#         for i in range(5):
#             row = [gen() for gen in data_generators]
#             rows.append(row)
            
#         writer.writerows(rows)
    
#     json_output = json.dumps(rows)
#     return json_output

# def generate_more_products():
#     filepath = Path(__file__).parent / "../data/data/products.csv"
#     schema_dict = PRODUCTS_SCHEMA
#     rows = []
#     with open(filepath, 'a', newline='') as file:
#         writer = csv.writer(file)
#         data_generators = [TYPES_TO_GENERATORS[elem['type']] for elem in schema_dict]

#         for i in range(3):
#             row = [gen() for gen in data_generators]
#             rows.append(row)
            
#         writer.writerows(rows)
        
#     json_output = json.dumps(rows)
#     return json_output

# def generate_more_orders():
#     filepath = Path(__file__).parent / "../data/data/orders.csv"
#     rows = []
#     with open(filepath, 'a', newline='') as file:
#         writer = csv.writer(file)
#         customers_id = pandas.read_csv(Path(__file__).parent / "../data/data/customers.csv")['cust_id'].to_list()
#         products_id = pandas.read_csv(Path(__file__).parent / "../data/data/products.csv")['prod_id'].to_list()
#         for i in range(5):
#             row = []
#             row.append(random_string())
#             row.append(random.choice(customers_id))
#             row.append(random.choice(products_id))
#             row.append(random.randint(1, 3))
            
#             rows.append(row)
            
#         writer.writerows(rows)
    
#     json_output = json.dumps(rows)
#     return json_output
       
       
def generate_more_customers():
    filepath = Path(__file__).parent / "../data/data/customer.csv"
    schema_dict = CUSTOMERS_SCHEMA
    data_list = []
    for i in range(5):
        data_object = {
            elem['name']: TYPES_TO_GENERATORS[elem['type']]() for elem in schema_dict
        }
        data_list.append(data_object)
    
    with open(filepath, 'a', newline='') as file:
        writer = csv.writer(file)
        for data_object in data_list:
            writer.writerow(data_object.values())
    
    return data_list


def generate_more_products():
    filepath = Path(__file__).parent / "../data/data/product.csv"
    schema_dict = PRODUCTS_SCHEMA
    data_list = []
    for i in range(3):
        data_object = {
            elem['name']: TYPES_TO_GENERATORS[elem['type']]() for elem in schema_dict
        }
        data_list.append(data_object)
    
    with open(filepath, 'a', newline='') as file:
        writer = csv.writer(file)
        for data_object in data_list:
            writer.writerow(data_object.values())
    
    return data_list


def generate_more_orders():
    filepath = Path(__file__).parent / "../data/data/order.csv"
    data_list = []
    customers_id = pandas.read_csv(Path(__file__).parent / "../data/data/customer.csv")['cust_id'].to_list()
    products_id = pandas.read_csv(Path(__file__).parent / "../data/data/product.csv")['prod_id'].to_list()
    for i in range(5):
        data_object = {
            'order_id': random_string(),
            'cust_id': random.choice(customers_id),
            'prod_id': random.choice(products_id),
            'count': random.randint(1, 3)
        }
        data_list.append(data_object)
    
    with open(filepath, 'a', newline='') as file:
        writer = csv.writer(file)
        for data_object in data_list:
            writer.writerow(data_object.values())
    
    return data_list


def hello():
    return "hello"
            
   
if __name__ == '__main__':
    # generate_file('customers', 'customers-50', 50)
    # generate_product()
    print(generate_more_orders())
    # generate_more_products()
    # generate_more_orders()