import random
import string
from faker import Faker

fake = Faker(use_weighting=False)

PIZZA = [
    "Pizza Napoletana",
    "Pizza Margherita",
    "Pizza alla diavola",
    "Pizza bufalina",
    "Pizza quattro formaggi",
    "Pizza capricious",
    "Pizzetta",
    "Pizza al taglio",
    "Calzones Pizza",
    "Pizza ai funghi",
    "Pizza Romana",
    "Pinsa romana",
    "Prosciutto e funghi pizza",
    "Kebab pizza",
    "Flammkuchen",
    "Dayton-style pizza",
    "Pissaladiere",
    "Lahmacun",
    "Sicilian",
    "Fugazza",
    "Pizza pho",
    "Pizza VN",
    "VN Pizza",
    "Brazilian Margherita pizza",
    "New York-style pizza",
    "Nova Scotian garlic fingers",
    "Domino's Cheesy Corn pizza",
    "Spicy Pizza Balado",
    "Tandoori Paneer pizza",
    "Mini-pizza Bazis"
]

TOPPING = [
    " - chocolate",
    " - ham",
    " - salami",
    " - mozarella",
    " - nuts",
    " - sausages",
    " - mocarella",
    " - peppers",
    " - chillies",
    " - rice",
    " - pineapples",
    " - durian",
    " - banana",
    " - tacos",
    " - turkey",
    " - fish"    
]

def random_string(len=15):
    lst =  [random.choice(string.hexdigits) for n in range(len)]
    return "".join(lst)

def sex():
    return random.choice(['Male', 'Female'])

def age():
    return random.randrange(10, 70)

def size():
    return random.randrange(1, 3)

def price():
    return random.randrange(20, 40) / 4

def product():
    return random.choice(PIZZA) + random.choice(TOPPING)

TYPES_TO_GENERATORS = {
    'id': random_string,
    'cust_name': fake.name,
    'sex': sex,
    'age': age,
    'address': fake.street_address,
    'phone': fake.phone_number,
    'job': fake.job,
    'price': price,
    'prod_name': product,
    # 'size': size,
    # 'price': fake.pricetag,
    # 'count': count
}

if __name__ == '__main__':
    print(product())