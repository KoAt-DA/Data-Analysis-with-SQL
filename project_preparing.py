from sqlalchemy import create_engine, Column, Integer, VARCHAR, DATE, DECIMAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from decouple import config

# Load the database URL from the configuration file and create a database engine.
# The config file should contain the following format:
# DB_URL = 'postgresql+psycopg2://YourUserName:YourPassword@localhost:5432/YourDatabaseName'

db_url = config('DB_URL')
engine = create_engine(db_url)


# Creating Tables
Base = declarative_base()

class Customer(Base):
    __tablename__= "Customers"

    Customer_ID = Column(Integer,primary_key=True)
    Name = Column(VARCHAR(255))
    Country = Column(VARCHAR(100))
    Age = Column(Integer)

    def __repr__(self):
        return f'<Customer(id={self.Customer_ID},name={self.Name},country={self.Country},age={self.Age})>'
    
class Product(Base):
    __tablename__ = "Products"

    Product_ID = Column(Integer,primary_key=True)
    Product_name = Column(VARCHAR(100))
    Price = Column(DECIMAL(10,2))
    Category = Column(VARCHAR(100))

    def __init__(self, Product_name, Price,Category):
        self.Product_name = Product_name
        self.Price = Price
        self.Category = Category

    def __repr__(self):
        return f'<Product(product_id={self.Product_ID}, product_name={self.Product_name}, price={self.Price}, category = {self.Category})>'
    
class Order(Base):
    __tablename__ = "Orders"

    Order_ID = Column(Integer,primary_key=True)
    Customer_ID = Column(Integer,ForeignKey('Customers.Customer_ID'))
    Order_Date = Column(DATE)
    Order_status = Column(VARCHAR(50))

    def __init__(self,Order_Date,Order_status,Customer_ID = None):
        self.Order_Date = Order_Date
        self.Order_status = Order_status
        self.Customer_ID = Customer_ID

    def __repr__(self):
        return f'<Order(order_id={self.Order_ID},customer={self.Customer_ID}, order_date={self.Order_Date}, order_status={self.Order_status})>'


class OrderDetail(Base):
    __tablename__ = "OrderDetails"

    OrderDetail_ID = Column(Integer, primary_key=True)
    Order_ID = Column(Integer, ForeignKey('Orders.Order_ID'))
    Product_ID = Column(Integer, ForeignKey('Products.Product_ID'))
    Quantity = Column(Integer)
    
    def __init__(self, Order_ID, Product_ID, Quantity):
        self.Order_ID = Order_ID
        self.Product_ID = Product_ID
        self.Quantity = Quantity

    def __repr__(self):
        return f'<OrderDetail(id={self.OrderDetail_ID}, order_id={self.Order_ID}, product_id={self.Product_ID}, quantity={self.Quantity})>'
    
# Base.metadata.create_all(engine)
# print("Tables created successfully!")    


# Upload datas to tables

session = Session(engine)


customers = [
    Customer(Name= 'Norma Fisher', Country= 'Germany', Age= 39),
    Customer(Name= 'Jorge Sullivan', Country= 'Italy', Age= 42),
    Customer(Name= 'Elizabeth Woods', Country= 'Canada', Age= 21),
    Customer(Name= 'Susan Wagner', Country= 'Spain', Age= 19),
    Customer(Name= 'Peter Montgomery', Country= 'Spain', Age= 40),
    Customer(Name= 'Theodore Mcgrath', Country= 'UK', Age= 76),
    Customer(Name= 'Stephanie Collins', Country= 'UK', Age= 42),
    Customer(Name= 'Stephanie Sutton', Country= 'USA', Age= 40),
    Customer(Name= 'Brian Hamilton', Country= 'Italy', Age= 62),
    Customer(Name= 'Susan Levy', Country= 'Spain', Age= 53),
    Customer(Name= 'Sean Green', Country= 'Italy', Age= 40),
    Customer(Name= 'Kimberly Smith', Country= 'USA', Age= 51),
    Customer(Name= 'Jennifer Summers', Country= 'UK', Age= 40),
    Customer(Name= 'April Snyder', Country= 'Spain', Age= 74),
    Customer(Name= 'Dana Nguyen', Country= 'Canada', Age= 30),
    Customer(Name= 'Cheryl Bradley', Country= 'UK', Age= 29),
    Customer(Name= 'Walter Pratt', Country= 'Spain', Age= 80),
    Customer(Name= 'Bobby Flores', Country= 'Canada', Age= 51),
    Customer(Name= 'Tasha Rodriguez', Country= 'Canada', Age= 25),
    Customer(Name= 'Michelle Kelley', Country= 'Spain', Age= 26),
    Customer(Name= 'Kimberly Maynard', Country= 'Canada', Age= 68),
    Customer(Name= 'Laurie Wallace', Country= 'Italy', Age= 37),
    Customer(Name= 'Janice Johnston', Country= 'Spain', Age= 56),
    Customer(Name= 'Collin Lopez', Country= 'Canada', Age= 22),
    Customer(Name= 'Mary Alvarez', Country= 'Canada', Age= 73),
    Customer(Name= 'Peter Mcdowell', Country= 'Italy', Age= 55),
    Customer(Name= 'Sarah Villanueva', Country= 'Italy', Age= 50),
    Customer(Name= 'Kimberly Myers', Country= 'USA', Age= 55),
    Customer(Name= 'Desiree Cain', Country= 'Canada', Age= 55),
    Customer(Name= 'Stephanie Lawrence', Country= 'Canada', Age= 68),
    Customer(Name= 'Lauren Hayes', Country= 'Canada', Age= 72),
    Customer(Name= 'Whitney Stark', Country= 'Spain', Age= 54),
    Customer(Name= 'Angela Salazar', Country= 'Germany', Age= 42),
    Customer(Name= 'Mr. Ryan Sanchez', Country= 'Canada', Age= 62),
    Customer(Name= 'Autumn Robinson', Country= 'USA', Age= 76),
    Customer(Name= 'Faith Cabrera', Country= 'Spain', Age= 73),
    Customer(Name= 'Charles Wolfe', Country= 'USA', Age= 32),
    Customer(Name= 'Kenneth Kent', Country= 'UK', Age= 74),
    Customer(Name= 'Melanie Johnson', Country= 'Spain', Age= 20),
    Customer(Name= 'Lisa Johnston', Country= 'Germany', Age= 43),
    Customer(Name= 'Jacob Hooper', Country= 'UK', Age= 23),
    Customer(Name= 'Alex Woodward', Country= 'Italy', Age= 35),
    Customer(Name= 'Caleb Clark', Country= 'UK', Age= 61),
    Customer(Name= 'Taylor Johnson', Country= 'Italy', Age= 41),
    Customer(Name= 'Brian Green', Country= 'Germany', Age= 29),
    Customer(Name= 'Matthew Bell', Country= 'USA', Age= 43),
    Customer(Name= 'Jonathan Williams', Country= 'UK', Age= 63),
    Customer(Name= 'William Gonzalez', Country= 'UK', Age= 70),
    Customer(Name= 'Nicholas Massey', Country= 'Germany', Age= 28),
    Customer(Name= 'Caroline Chambers', Country= 'Spain', Age= 62)
]

# session.add_all(customers)
# session.commit()
# print("Customers table uploaded!")

products = [
    Product(Product_name='Laptop', Price=799.99, Category='Electronics'),
    Product(Product_name='Smartphone', Price=499.99, Category='Electronics'),
    Product(Product_name='Headphones', Price=89.99, Category='Electronics'),
    Product(Product_name='Smartwatch', Price=199.99, Category='Electronics'),
    Product(Product_name='TV', Price=349.99, Category='Electronics'),
    Product(Product_name='Basketball', Price=29.99, Category='Sport'),
    Product(Product_name='Soccer Ball', Price=19.99, Category='Sport'),
    Product(Product_name='Tennis Racket', Price=59.99, Category='Sport'),
    Product(Product_name='Football', Price=24.99, Category='Sport'),
    Product(Product_name='Yoga Mat', Price=19.99, Category='Sport'),
    Product(Product_name='T-Shirt', Price=15.99, Category='Clothing'),
    Product(Product_name='Jeans', Price=39.99, Category='Clothing'),
    Product(Product_name='Jacket', Price=59.99, Category='Clothing'),
    Product(Product_name='Shoes', Price=69.99, Category='Clothing'),
    Product(Product_name='Sweater', Price=34.99, Category='Clothing'),
    Product(Product_name='Backpack', Price=49.99, Category='Clothing'),
    Product(Product_name='Watch', Price=119.99, Category='Clothing'),
    Product(Product_name='Belt', Price=19.99, Category='Clothing'),
    Product(Product_name='Cap', Price=14.99, Category='Clothing'),
    Product(Product_name='Sunglasses', Price=29.99, Category='Clothing')
]

# session.add_all(products)
# session.commit()
# print("Products table uploaded!")


orders = [
    Order(Order_Date='2024-05-02', Order_status='Paid', Customer_ID=1),
    Order(Order_Date='2024-03-28', Order_status='Paid', Customer_ID=2),
    Order(Order_Date='2024-02-17', Order_status='Pending', Customer_ID=3),
    Order(Order_Date='2024-01-19', Order_status='Shipped', Customer_ID=4),
    Order(Order_Date='2024-04-03', Order_status='Paid', Customer_ID=5),
    Order(Order_Date='2024-03-15', Order_status='Paid', Customer_ID=6),
    Order(Order_Date='2024-01-08', Order_status='Pending', Customer_ID=1),
    Order(Order_Date='2023-12-05', Order_status='Shipped', Customer_ID=2),
    Order(Order_Date='2024-06-17', Order_status='Paid', Customer_ID=3),
    Order(Order_Date='2024-01-25', Order_status='Shipped', Customer_ID=4),
    Order(Order_Date='2024-02-06', Order_status='Shipped', Customer_ID=5),
    Order(Order_Date='2024-07-19', Order_status='Paid', Customer_ID=6),
    Order(Order_Date='2024-06-25', Order_status='Paid', Customer_ID=8),
    Order(Order_Date='2024-01-17', Order_status='Paid', Customer_ID=9),
    Order(Order_Date='2024-04-12', Order_status='Shipped', Customer_ID=10),
    Order(Order_Date='2024-06-20', Order_status='Paid', Customer_ID=9),
    Order(Order_Date='2024-02-25', Order_status='Pending', Customer_ID=10),
    Order(Order_Date='2024-03-13', Order_status='Shipped', Customer_ID=6),
    Order(Order_Date='2023-12-30', Order_status='Paid', Customer_ID=4),
    Order(Order_Date='2024-01-03', Order_status='Pending', Customer_ID=2),
    Order(Order_Date='2024-06-21', Order_status='Shipped', Customer_ID=3),
    Order(Order_Date='2024-03-10', Order_status='Paid', Customer_ID=1),
    Order(Order_Date='2024-01-13', Order_status='Shipped', Customer_ID=5),
    Order(Order_Date='2024-03-22', Order_status='Paid', Customer_ID=2),
    Order(Order_Date='2024-05-18', Order_status='Shipped', Customer_ID=9),
    Order(Order_Date='2024-07-15', Order_status='Paid', Customer_ID=6),
    Order(Order_Date='2024-03-17', Order_status='Shipped', Customer_ID=4),
    Order(Order_Date='2024-06-03', Order_status='Pending', Customer_ID=1),
    Order(Order_Date='2024-02-19', Order_status='Paid', Customer_ID=5),
    Order(Order_Date='2024-05-21', Order_status='Shipped', Customer_ID=10),
    Order(Order_Date='2024-02-01', Order_status='Paid', Customer_ID=3),
    Order(Order_Date='2024-07-12', Order_status='Paid', Customer_ID=11),
    Order(Order_Date='2024-06-01', Order_status='Pending', Customer_ID=12),
    Order(Order_Date='2024-07-21', Order_status='Shipped', Customer_ID=14),
    Order(Order_Date='2024-05-15', Order_status='Paid', Customer_ID=15),
    Order(Order_Date='2024-06-23', Order_status='Shipped', Customer_ID=16),
    Order(Order_Date='2024-07-02', Order_status='Paid', Customer_ID=17),
    Order(Order_Date='2024-01-12', Order_status='Paid', Customer_ID=18),
    Order(Order_Date='2024-07-11', Order_status='Shipped', Customer_ID=19),
    Order(Order_Date='2024-03-04', Order_status='Pending', Customer_ID=20),
    Order(Order_Date='2024-06-28', Order_status='Paid', Customer_ID=21),
    Order(Order_Date='2024-02-19', Order_status='Shipped', Customer_ID=22),
    Order(Order_Date='2024-05-07', Order_status='Paid', Customer_ID=23),
    Order(Order_Date='2024-04-22', Order_status='Paid', Customer_ID=24),
    Order(Order_Date='2024-06-10', Order_status='Paid', Customer_ID=25),
    Order(Order_Date='2024-07-14', Order_status='Shipped', Customer_ID=11),
    Order(Order_Date='2024-06-15', Order_status='Shipped', Customer_ID=12),
    Order(Order_Date='2024-04-11', Order_status='Paid', Customer_ID=15),
    Order(Order_Date='2024-02-23', Order_status='Shipped', Customer_ID=16),
    Order(Order_Date='2024-05-01', Order_status='Paid', Customer_ID=17),
    Order(Order_Date='2024-07-01', Order_status='Paid', Customer_ID=19),
    Order(Order_Date='2024-06-05', Order_status='Shipped', Customer_ID=20),
    Order(Order_Date='2024-07-03', Order_status='Paid', Customer_ID=22),
    Order(Order_Date='2024-03-13', Order_status='Shipped', Customer_ID=23),
    Order(Order_Date='2024-04-18', Order_status='Shipped', Customer_ID=24),
    Order(Order_Date='2024-07-18', Order_status='Paid', Customer_ID=25),
    Order(Order_Date='2024-02-03', Order_status='Shipped', Customer_ID=11),
    Order(Order_Date='2024-06-20', Order_status='Paid', Customer_ID=19),
    Order(Order_Date='2024-07-06', Order_status='Shipped', Customer_ID=12),
    Order(Order_Date='2024-05-26', Order_status='Paid', Customer_ID=17),
    Order(Order_Date='2024-03-09', Order_status='Paid', Customer_ID=21),
    Order(Order_Date='2024-06-12', Order_status='Shipped', Customer_ID=18),
    Order(Order_Date='2024-04-08', Order_status='Paid', Customer_ID=24),
    Order(Order_Date='2024-07-05', Order_status='Paid', Customer_ID=16),
    Order(Order_Date='2024-05-20', Order_status='Paid', Customer_ID=26),
    Order(Order_Date='2024-06-15', Order_status='Shipped', Customer_ID=27),
    Order(Order_Date='2024-07-09', Order_status='Paid', Customer_ID=28),
    Order(Order_Date='2024-03-22', Order_status='Shipped', Customer_ID=29),
    Order(Order_Date='2024-04-30', Order_status='Paid', Customer_ID=30),
    Order(Order_Date='2024-02-10', Order_status='Shipped', Customer_ID=31),
    Order(Order_Date='2024-06-25', Order_status='Paid', Customer_ID=32),
    Order(Order_Date='2024-07-15', Order_status='Paid', Customer_ID=34),
    Order(Order_Date='2024-04-05', Order_status='Paid', Customer_ID=35),
    Order(Order_Date='2024-06-10', Order_status='Paid', Customer_ID=36),
    Order(Order_Date='2024-01-17', Order_status='Shipped', Customer_ID=38),
    Order(Order_Date='2024-07-11', Order_status='Shipped', Customer_ID=39),
    Order(Order_Date='2024-02-28', Order_status='Paid', Customer_ID=40),
    Order(Order_Date='2024-06-08', Order_status='Shipped', Customer_ID=26),
    Order(Order_Date='2024-03-15', Order_status='Paid', Customer_ID=27),
    Order(Order_Date='2024-06-27', Order_status='Paid', Customer_ID=28),
    Order(Order_Date='2024-02-23', Order_status='Paid', Customer_ID=29),
    Order(Order_Date='2024-06-03', Order_status='Shipped', Customer_ID=30),
    Order(Order_Date='2024-04-22', Order_status='Shipped', Customer_ID=31),
    Order(Order_Date='2024-05-18', Order_status='Paid', Customer_ID=32),
    Order(Order_Date='2024-03-30', Order_status='Paid', Customer_ID=34),
    Order(Order_Date='2024-06-19', Order_status='Paid', Customer_ID=35),
    Order(Order_Date='2024-07-05', Order_status='Shipped', Customer_ID=36),
    Order(Order_Date='2024-05-25', Order_status='Paid', Customer_ID=38),
    Order(Order_Date='2024-02-16', Order_status='Paid', Customer_ID=39),
    Order(Order_Date='2024-07-01', Order_status='Shipped', Customer_ID=40),
    Order(Order_Date='2024-04-18', Order_status='Paid', Customer_ID=26),
    Order(Order_Date='2024-03-12', Order_status='Shipped', Customer_ID=27),
    Order(Order_Date='2024-05-05', Order_status='Shipped', Customer_ID=29),
    Order(Order_Date='2024-07-13', Order_status='Paid', Customer_ID=30),
    Order(Order_Date='2024-06-12', Order_status='Paid', Customer_ID=41),
    Order(Order_Date='2024-03-01', Order_status='Shipped', Customer_ID=42),
    Order(Order_Date='2024-05-10', Order_status='Paid', Customer_ID=43),
    Order(Order_Date='2024-04-05', Order_status='Paid', Customer_ID=44),
    Order(Order_Date='2024-06-21', Order_status='Shipped', Customer_ID=45),
    Order(Order_Date='2024-01-25', Order_status='Paid', Customer_ID=46),
    Order(Order_Date='2024-02-14', Order_status='Shipped', Customer_ID=47),
    Order(Order_Date='2024-07-09', Order_status='Paid', Customer_ID=48),
    Order(Order_Date='2024-04-15', Order_status='Shipped', Customer_ID=49),
    Order(Order_Date='2024-03-17', Order_status='Paid', Customer_ID=50),
    Order(Order_Date='2024-02-11', Order_status='Shipped', Customer_ID=41),
    Order(Order_Date='2024-05-01', Order_status='Paid', Customer_ID=42),
    Order(Order_Date='2024-07-20', Order_status='Shipped', Customer_ID=43),
    Order(Order_Date='2024-06-17', Order_status='Paid', Customer_ID=44),
    Order(Order_Date='2024-07-02', Order_status='Shipped', Customer_ID=45),
    Order(Order_Date='2024-03-25', Order_status='Paid', Customer_ID=46),
    Order(Order_Date='2024-01-17', Order_status='Shipped', Customer_ID=47),
    Order(Order_Date='2024-06-28', Order_status='Paid', Customer_ID=48),
    Order(Order_Date='2024-04-27', Order_status='Paid', Customer_ID=49),
    Order(Order_Date='2024-07-13', Order_status='Shipped', Customer_ID=50),
    Order(Order_Date='2024-05-06', Order_status='Paid', Customer_ID=41),
    Order(Order_Date='2024-02-25', Order_status='Shipped', Customer_ID=42),
    Order(Order_Date='2024-03-29', Order_status='Paid', Customer_ID=43),
    Order(Order_Date='2024-06-08', Order_status='Paid', Customer_ID=44),
    Order(Order_Date='2024-01-31', Order_status='Shipped', Customer_ID=45),
    Order(Order_Date='2024-05-18', Order_status='Shipped', Customer_ID=46),
    Order(Order_Date='2024-07-06', Order_status='Paid', Customer_ID=47),
    Order(Order_Date='2024-06-24', Order_status='Shipped', Customer_ID=48),
    Order(Order_Date='2024-02-07', Order_status='Paid', Customer_ID=49),
    Order(Order_Date='2024-04-12', Order_status='Paid', Customer_ID=50)
]

# session.add_all(orders)
# session.commit()
# print("Orders table uploaded!")


orderdetails = [
    OrderDetail(Order_ID=1, Product_ID=3, Quantity=2),
    OrderDetail(Order_ID=2, Product_ID=4, Quantity=1),
    OrderDetail(Order_ID=3, Product_ID=2, Quantity=3),
    OrderDetail(Order_ID=4, Product_ID=1, Quantity=1),
    OrderDetail(Order_ID=5, Product_ID=6, Quantity=5),
    OrderDetail(Order_ID=6, Product_ID=5, Quantity=2),
    OrderDetail(Order_ID=7, Product_ID=3, Quantity=1),
    OrderDetail(Order_ID=8, Product_ID=2, Quantity=4),
    OrderDetail(Order_ID=9, Product_ID=7, Quantity=3),
    OrderDetail(Order_ID=10, Product_ID=1, Quantity=2),
    OrderDetail(Order_ID=11, Product_ID=8, Quantity=1),
    OrderDetail(Order_ID=12, Product_ID=2, Quantity=3),
    OrderDetail(Order_ID=13, Product_ID=5, Quantity=2),
    OrderDetail(Order_ID=14, Product_ID=9, Quantity=6),
    OrderDetail(Order_ID=15, Product_ID=10, Quantity=3),
    OrderDetail(Order_ID=16, Product_ID=3, Quantity=4),
    OrderDetail(Order_ID=17, Product_ID=6, Quantity=7),
    OrderDetail(Order_ID=18, Product_ID=7, Quantity=2),
    OrderDetail(Order_ID=19, Product_ID=8, Quantity=3),
    OrderDetail(Order_ID=20, Product_ID=9, Quantity=1),
    OrderDetail(Order_ID=21, Product_ID=4, Quantity=4),
    OrderDetail(Order_ID=22, Product_ID=10, Quantity=3),
    OrderDetail(Order_ID=23, Product_ID=5, Quantity=6),
    OrderDetail(Order_ID=24, Product_ID=1, Quantity=4),
    OrderDetail(Order_ID=25, Product_ID=6, Quantity=5),
    OrderDetail(Order_ID=26, Product_ID=2, Quantity=2),
    OrderDetail(Order_ID=27, Product_ID=9, Quantity=6),
    OrderDetail(Order_ID=28, Product_ID=4, Quantity=1),
    OrderDetail(Order_ID=29, Product_ID=10, Quantity=3),
    OrderDetail(Order_ID=30, Product_ID=5, Quantity=5),
    OrderDetail(Order_ID=31, Product_ID=3, Quantity=2),
    OrderDetail(Order_ID=32, Product_ID=5, Quantity=1),
    OrderDetail(Order_ID=33, Product_ID=6, Quantity=3),
    OrderDetail(Order_ID=34, Product_ID=2, Quantity=5),
    OrderDetail(Order_ID=35, Product_ID=8, Quantity=4),
    OrderDetail(Order_ID=36, Product_ID=3, Quantity=2),
    OrderDetail(Order_ID=37, Product_ID=7, Quantity=6),
    OrderDetail(Order_ID=38, Product_ID=1, Quantity=1),
    OrderDetail(Order_ID=39, Product_ID=9, Quantity=3),
    OrderDetail(Order_ID=40, Product_ID=10, Quantity=2),
    OrderDetail(Order_ID=41, Product_ID=4, Quantity=2),
    OrderDetail(Order_ID=42, Product_ID=5, Quantity=3),
    OrderDetail(Order_ID=43, Product_ID=6, Quantity=5),
    OrderDetail(Order_ID=44, Product_ID=8, Quantity=2),
    OrderDetail(Order_ID=45, Product_ID=2, Quantity=6),
    OrderDetail(Order_ID=46, Product_ID=7, Quantity=4),
    OrderDetail(Order_ID=47, Product_ID=10, Quantity=2),
    OrderDetail(Order_ID=48, Product_ID=1, Quantity=3),
    OrderDetail(Order_ID=49, Product_ID=4, Quantity=2),
    OrderDetail(Order_ID=50, Product_ID=3, Quantity=1),
    OrderDetail(Order_ID=51, Product_ID=5, Quantity=4),
    OrderDetail(Order_ID=52, Product_ID=9, Quantity=2),
    OrderDetail(Order_ID=53, Product_ID=6, Quantity=3),
    OrderDetail(Order_ID=54, Product_ID=2, Quantity=5),
    OrderDetail(Order_ID=55, Product_ID=7, Quantity=4),
    OrderDetail(Order_ID=56, Product_ID=9, Quantity=1),
    OrderDetail(Order_ID=57, Product_ID=3, Quantity=3),
    OrderDetail(Order_ID=58, Product_ID=5, Quantity=5),
    OrderDetail(Order_ID=59, Product_ID=10, Quantity=2),
    OrderDetail(Order_ID=60, Product_ID=4, Quantity=6),
    OrderDetail(Order_ID=61, Product_ID=4, Quantity=2),
    OrderDetail(Order_ID=62, Product_ID=8, Quantity=3),
    OrderDetail(Order_ID=63, Product_ID=2, Quantity=1),
    OrderDetail(Order_ID=64, Product_ID=7, Quantity=5),
    OrderDetail(Order_ID=65, Product_ID=1, Quantity=4),
    OrderDetail(Order_ID=66, Product_ID=3, Quantity=2),
    OrderDetail(Order_ID=67, Product_ID=6, Quantity=3),
    OrderDetail(Order_ID=68, Product_ID=5, Quantity=6),
    OrderDetail(Order_ID=69, Product_ID=10, Quantity=1),
    OrderDetail(Order_ID=70, Product_ID=4, Quantity=2),
    OrderDetail(Order_ID=71, Product_ID=7, Quantity=4),
    OrderDetail(Order_ID=72, Product_ID=9, Quantity=3),
    OrderDetail(Order_ID=73, Product_ID=8, Quantity=3),
    OrderDetail(Order_ID=74, Product_ID=5, Quantity=5),
    OrderDetail(Order_ID=75, Product_ID=6, Quantity=1),
    OrderDetail(Order_ID=76, Product_ID=7, Quantity=2),
    OrderDetail(Order_ID=77, Product_ID=9, Quantity=3),
    OrderDetail(Order_ID=78, Product_ID=4, Quantity=6),
    OrderDetail(Order_ID=79, Product_ID=3, Quantity=2),
    OrderDetail(Order_ID=80, Product_ID=2, Quantity=4),
    OrderDetail(Order_ID=81, Product_ID=10, Quantity=5),
    OrderDetail(Order_ID=82, Product_ID=8, Quantity=4),
    OrderDetail(Order_ID=83, Product_ID=5, Quantity=2),
    OrderDetail(Order_ID=84, Product_ID=6, Quantity=6),
    OrderDetail(Order_ID=85, Product_ID=7, Quantity=3),
    OrderDetail(Order_ID=86, Product_ID=4, Quantity=2),
    OrderDetail(Order_ID=87, Product_ID=10, Quantity=3),
    OrderDetail(Order_ID=88, Product_ID=1, Quantity=3),
    OrderDetail(Order_ID=89, Product_ID=8, Quantity=4),
    OrderDetail(Order_ID=90, Product_ID=5, Quantity=3),
    OrderDetail(Order_ID=91, Product_ID=4, Quantity=1),
    OrderDetail(Order_ID=92, Product_ID=6, Quantity=2),
    OrderDetail(Order_ID=93, Product_ID=7, Quantity=1),
    OrderDetail(Order_ID=94, Product_ID=10, Quantity=3),
    OrderDetail(Order_ID=95, Product_ID=2, Quantity=4),
    OrderDetail(Order_ID=96, Product_ID=1, Quantity=2),
    OrderDetail(Order_ID=97, Product_ID=5, Quantity=1),
    OrderDetail(Order_ID=98, Product_ID=9, Quantity=2),
    OrderDetail(Order_ID=99, Product_ID=8, Quantity=5),
    OrderDetail(Order_ID=100, Product_ID=6, Quantity=3),
    OrderDetail(Order_ID=101, Product_ID=4, Quantity=6),
    OrderDetail(Order_ID=102, Product_ID=2, Quantity=2),
    OrderDetail(Order_ID=103, Product_ID=3, Quantity=3),
    OrderDetail(Order_ID=104, Product_ID=9, Quantity=1),
    OrderDetail(Order_ID=105, Product_ID=7, Quantity=3),
    OrderDetail(Order_ID=106, Product_ID=10, Quantity=4),
    OrderDetail(Order_ID=107, Product_ID=8, Quantity=1),
    OrderDetail(Order_ID=108, Product_ID=5, Quantity=3),
    OrderDetail(Order_ID=109, Product_ID=6, Quantity=2),
    OrderDetail(Order_ID=110, Product_ID=4, Quantity=3),
    OrderDetail(Order_ID=111, Product_ID=3, Quantity=5),
    OrderDetail(Order_ID=112, Product_ID=9, Quantity=2),
    OrderDetail(Order_ID=113, Product_ID=7, Quantity=1),
    OrderDetail(Order_ID=114, Product_ID=10, Quantity=2),
    OrderDetail(Order_ID=115, Product_ID=1, Quantity=6),
    OrderDetail(Order_ID=116, Product_ID=5, Quantity=1),
    OrderDetail(Order_ID=117, Product_ID=6, Quantity=4),
    OrderDetail(Order_ID=118, Product_ID=4, Quantity=2),
    OrderDetail(Order_ID=119, Product_ID=8, Quantity=3),
    OrderDetail(Order_ID=120, Product_ID=3, Quantity=3),
    OrderDetail(Order_ID=121, Product_ID=2, Quantity=3),
    OrderDetail(Order_ID=122, Product_ID=5, Quantity=2),
    OrderDetail(Order_ID=123, Product_ID=7, Quantity=4),
    OrderDetail(Order_ID=124, Product_ID=10, Quantity=1)
]

# session.add_all(orderdetails)
# session.commit()
# print("Orderdetails table uploaded!")