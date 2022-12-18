from sqlalchemy import MetaData, Table, Column, Integer, String, DECIMAL,\
     Boolean, ForeignKeyConstraint, Enum, Date, create_engine

engine = create_engine('postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:${POSTGRES_PORT}/${POSTGRES_DB}', echo=True)
meta = MetaData()

product_category = Table(
    'product_category',
    meta,
    Column('category_id', Integer, primary_key=True),
    Column('category_name', String(255))
)

discounts = Table(
    'discounts',
    meta,
    Column('discount_id', Integer, primary_key=True),
    Column('discount_name', String(255)),
    Column('discount_percent', DECIMAL(4, 2)),
    Column('active_discount', Boolean)
)

# change size and color to enum later
products = Table(
    'products',
    meta,
    Column('product_id', Integer, primary_key=True),
    Column('product_name', String(255)),
    Column('size', String(255)),
    Column('price', DECIMAL(4, 2)),
    Column('product_quantity', Integer),
    Column('color', String(255))
)

product_categories = Table(
    'product_categories',
    meta,
    Column('product_id', Integer, primary_key=True),
    Column('category_id', Integer, primary_key=True),
    Column('discount_id', Integer, primary_key=True),
    ForeignKeyConstraint(
        ['product_id', 'category_id', 'discount_id'],
        ['products.product_id', 'product_category.category_id', 'discounts.discount_id']
    )
)

cart = Table(
    'cart',
    meta,
    Column('user_id', Integer, primary_key=True),
    Column('product_id', Integer, primary_key=True),
    Column('cart_quantity', Integer),
    ForeignKeyConstraint(
        ['user_id', 'product_id'],
        ['users.user_id', 'products.product_id']
    )
)

users = Table(
    'users',
    meta,
    Column('user_id', Integer, primary_key=True),
    Column('user_role', Boolean),
    Column('first_name', String(255)),
    Column('last_name', String(255)),
    Column('email', String(255)),
    Column('password', String(255))
)

user_address = Table(
    'user_address',
    meta,
    Column('user_id', Integer, primary_key=True),
    Column('address_line', String(255)),
    Column('city', String(255)),
    Column('postal_code', Integer),
    Column('phone', String(255)),
    ForeignKeyConstraint(
        ['user_id'],
        ['users.user_id']
    )
)

user_payment = Table(
    'user_payment',
    meta,
    Column('payment_id', Integer, primary_key=True),
    Column('user_id', Integer, primary_key=True),
    Column('order_id', Integer, primary_key=True),
    Column('card_number', Integer),
    Column('ccv', Integer),
    Column('exp_date', Date),
    ForeignKeyConstraint(
        ['user_id', 'order_id'],
        ['users.user_id', 'orders.order_id']
    )
)

orders = Table(
    'orders',
    meta,
    Column('order_id', Integer, primary_key=True),
    Column('user_id', Integer, primary_key=True),
    Column('first_name', String(255)),
    Column('last_name', String(255)),
    Column('email', String(255)),
    ForeignKeyConstraint(
        ['user_id'],
        ['users.user_id']
    )
)

product_orders = Table(
    'product_orders',
    meta,
    Column('order_id', Integer, primary_key=True),
    Column('item_name', String(255)),
    Column('item_price', DECIMAL(4, 2)),
    Column('item_quantity', Integer),
    ForeignKeyConstraint(
        ['order_id'],
        ['orders.order_id']
    )
)

order_totals = Table(
    'order_totals',
    meta,
    Column('total_id', Integer, primary_key=True),
    Column('order_id', Integer, primary_key=True),
    Column('total_amount', DECIMAL(4, 2)),
    ForeignKeyConstraint(
        ['order_id'],
        ['orders.order_id']
    )
)

# create user_address, user_payment, orders, order_products, and order totals

meta.create_all(engine)
