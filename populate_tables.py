from sqlalchemy import create_engine, MetaData, select
from faker import Faker
import sys
import random
import datetime

engine = create_engine('postgresql://postgres:postgres@localhost:5432/cabbage_corp')
meta = MetaData()

faker = Faker()

# reflects tables/schema already existing in postgres database
with engine.connect() as conn:
    meta.reflect(conn)

# print(meta.tables)
# Creates table objects
product_category = meta.tables['product_category']
# discounts = meta.tables.keys['discounts']
# products = meta.tables.keys['products']
# product_categories = meta.tables.keys['product_categories']
# cart = meta.tables.keys['cart']
# users = meta.tables.keys['users']
# user_address = meta.tables.keys['user_address']
# orders = meta.tables.keys['orders']
# product_orders = meta.tables.keys['product_orders']
# order_totals = meta.tables.keys['order_totals']
# user_payment = meta.tables.keys['user_payment']

# list of fake cabbage_corp products
product_list = ['boots', 'sneakers', 'sweater', 'hat', 'shirt', 'shorts', 'jeans', \
    'hat', 'beanies', 'sunglasses']
category_list = ['shoes', 'accessories', 'tops', 'bottoms']

# class used to generate data for tables
class GenerateData:
    def __init__(self):
        # first input
        self.table = sys.argv[1]
        # second input this is using vim!
        self.num = int(sys.argv[2])
    
    def create_data(self):
        # uses faker library to generate and insert data
        # this checkkjdfldjfljldkfjldklj;as if table doesn't exist in database
        if self.table not in meta.tables.keys():
            return print(f'{self.table} does not exist')
        
        if self.table == 'product_category':
            with engine.begin() as conn:
                for _ in range(self.num):
                    stmt = product_category.insert().values(
                        category_name = random.choice(category_list)
                    )
                    conn.execute(stmt)

        if self.table == 'discounts':
            ...

        if self.table == 'products':
            ...

        if self.table == 'product_categories':
            ...

        if self.table == 'cart':
            ...
        
        if self.table == 'users':
            ...
        
        if self.table == 'user_address':
            ...
        
        if self.table == 'orders':
            ...
        
        if self.table == 'product_orders':
            ...

        if self.table == 'order_totals':
            ...
        
        if self.table == 'user_payment':
            ...


if __name__ == "__main__":    
    generate_data = GenerateData()   
    generate_data.create_data()
