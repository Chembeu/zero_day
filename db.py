from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text,  DateTime, Boolean
from datetime import datetime
from sqlalchemy.sql import insert
# Connection to the MySQL database
engine = create_engine('mysql+mysqlconnector://root:7629@localhost:3306/rental_house', echo=True)
connection = engine.connect()
    #Always Use text for Raw SQL Queries: The text function wraps raw SQL 
    # strings into executable SQL statements that SQLAlchemy understands.
query = text("SELECT * FROM payments")
result = connection.execute(query)

    # Fetch all rows
tenants = result.fetchall()
for row in tenants:
        print (row)
metadata = MetaData()
rent = Table ( 'rent',metadata,
    Column('id', Integer(), primary_key=True),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)
metadata.create_all(engine)
insert_stmt = insert(rent).values(
        id=1  # Explicitly set the ID (optional if using autoincrement)
    )

    # Execute the insert statement
connection.execute(insert_stmt)

    # Query the data to confirm the insertion
ret = connection.execute(rent.select())
for row in ret:
     print(row)
    