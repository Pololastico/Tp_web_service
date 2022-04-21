from sqlalchemy import create_engine

db_string = "postgresql://root:root@localhost:5432/store"

engine = create_engine(db_string)
connection = engine.connect()

# Create 
#connection.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")  
#connection.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

#TP
with open ("src\create_table.sql") as create_table:
    #print(create_table.read())
    connection.execute(create_table.read())


    




