import pandas as pd
import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/application')


https://pandas.pydata.org/pandas-docs/stable/io.html#engine-connection-examples // TO CHECK SOME INFO I COULD NEED FOR OTHER SQL FORMS

# //READ ENTIRE TABLE
df = pd.read_sql_table('customers',engine)

# //READ ONLY SELECTED COLUMNS
df = pd.read_sql_table('customers', engine, columns=["name"])

# READ WITH SQL QUERY JOIN

query = '''
 SELECT customers.name, customers.phone_number, orders.name, orders.amount
 FROM customers INNER JOIN orders
 ON customers.id=orders.customer_id
'''

df = pd.read_sql_query(query,engine)


# //RENAME COLUMNS
df = pd.read_csv("customers.csv")
df.rename(columns={
    'Customer Name': 'name',
    'Customer Phone': 'phone_number'
}, inplace=True)


# // WRITE TO MYSQL USING TO_sQL
df.to_sql(
    name='customers', # database table name
    con=engine,
    if_exists='append',
    index=False
)
