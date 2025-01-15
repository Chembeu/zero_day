from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Connection to the MySQL database
engine = create_engine('mysql+mysqlconnector://root:7629@localhost:3306/rental_house', echo=True)
with engine.connect() as connenction:
    tenants = connenction.execute("SELECT * FROM payments")
    for row in tenants:
        print (row)