
import pandas as pd
from sqlalchemy import create_engine

# RDS connection details
user = 'admin'
password = 'Adfpu$6813'
host = 'croma-db.cnksq8s8gfwo.us-east-1.rds.amazonaws.com'
port = '3306'
database = 'cromadb'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')

required_columns = [
    'Manufacturer_Acer', 'Manufacturer_Apple', 'Manufacturer_Asus',
    'Manufacturer_Dell', 'Manufacturer_Fujitsu', 'Manufacturer_HP',
    'Manufacturer_Lenovo', 'Manufacturer_MSI', 'Manufacturer_Microsoft',
    'Manufacturer_Samsung', 'Product_Code', 'MRP_Price', 'Discounted_Price',
    'Rating_Out_Of_5', 'Num_Of_Ratings', 'Mac', 'Ultra Thin Laptops',
    'Windows', 'Gaming Laptops', '2-In-1 Laptops',
    'Content Creation Laptops', 'Thin & Light Laptops', 'AI Ready Laptops',
    'RAM', 'ROM'
]

for col in required_columns:
    if col not in df.columns:
        df[col] = None 

df.to_sql('croma_laptop_data', con=engine, if_exists='replace', index=False)

print("Data uploaded successfully!")

