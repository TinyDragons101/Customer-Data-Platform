import csv
from pathlib import Path
from zipfile import ZipFile, ZIP_BZIP2

from generators import (
    TYPES_TO_GENERATORS,
    PRODUCTS
)

from schemas import (
    CUSTOMERS_SCHEMA,
    PRODUCTS_SCHEMA,
    ORDERS_SCHEMA
)

SCHEMA_TO_DICT = {
    'customers': CUSTOMERS_SCHEMA,
    'products': PRODUCTS_SCHEMA,
    'orders': ORDERS_SCHEMA
}


def generate_file(schema='customers', name="customers-10000", count=1000000):
    p = Path(__file__).parent / "../data"
    p.mkdir(parents=True, exist_ok=True)

    file_name = "{}.csv".format(name)
    file_path = p / file_name

    if file_path.exists():
        schema_dict = SCHEMA_TO_DICT[schema]

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            # Headers
            headers = [elem['name'] for elem in schema_dict]
            headers.insert(0, "Index") # Add an Index header
            writer.writerow(headers)

            # Content
            data_generators = [TYPES_TO_GENERATORS[elem['type']] for elem in schema_dict]

            rows = []
            for index in range(1, count+1):
                row = [gen() for gen in data_generators]
                row.insert(0, index)
                rows.append(row)

                if index % 1000 == 0:
                    writer.writerows(rows)
                    rows = []

                if index % 10000 == 0:
                    print("{}/{}".format(index, count))

            writer.writerows(rows)
    # else:
    #     print("{} already exists".format(file_path))

def generate_product():
    file_name = "products.csv"
    file_path = Path(__file__).parent / "../data" / file_name
    
    if file_path.exists():
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # Headers
            headers = [elem['name'] for elem in PRODUCTS_SCHEMA]
            headers.insert(0, "Index")
            writer.writerow(headers)
            rows = []
            # Content
            index = 1
            for product in PRODUCTS:
                for size in range(1, 4):
                    row = [index]
                    row.append(TYPES_TO_GENERATORS['id']())
                    row.append(product)
                    row.append(size)
                    row.append(TYPES_TO_GENERATORS['price']() * size)
                    rows.append(row)
                    index = index + 1
                
            writer.writerows(rows)
    # else:
    #     print("{} already exists".format(file_path))
                    
                
if __name__ == '__main__':
    generate_file('customers', 'customers-200', 200)
    generate_product()