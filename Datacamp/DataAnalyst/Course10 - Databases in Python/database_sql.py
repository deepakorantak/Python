# Import create_engine
from sqlalchemy import create_engine,Table,select

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')


metadata = Metadata()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

connect = engine.connect()

# Build select statement for census table: stmt
stmt = 'select * from census'

# Execute the statement and fetch the results: results
results = connection.execute(stmt).fetchall()

# Print Results
print(results)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL emitted
print(stmt)

# Execute the statement and print the results
print(connection.execute(stmt).fetchall())

# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by using an index
print(first_row[0])

# Print the 'state' column of the first row by using its name
print(first_row['state'])






