import requests
import json

def extract_customers_api():
    response = requests.get('http://127.0.0.1:8000/generate_data/customers')
    data = response.json()
    with open('../data/raw_data/raw_customers.json', 'w') as f:
        json.dump(data, f)
    return response.json()
            
if __name__ == '__main__':
    print(extract_customers_api())