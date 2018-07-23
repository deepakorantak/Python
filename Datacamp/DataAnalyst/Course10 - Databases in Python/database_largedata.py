# Import create_engine function
from sqlalchemy import create_engine,select,order_by,desc,group_by,alias

# Create an engine to the census database
engine = create_engine('sqlite:///census.sqlite')
metadata = Metadata()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

connection = engine.connect()
#----------------------------------------------------------------------------------------------------

stmt = select([census])
results_proxy = connection.execute(stmt)
more_results = True
state_count = {}

# Start a while loop checking for more results
while more_results:
    # Fetch the first 50 results from the ResultProxy: partial_results
    partial_results = results_proxy.fetchmany(50)

    # if empty list, set more_results to False
    if partial_results == []:
        more_results = False

    # Loop over the fetched records and increment the count for the state
    for row in partial_results:
        if row.state in state_count:
            state_count[row.state] += 1
        else:
            state_count[row.state] = 1

# Close the ResultProxy, and thus the connection
results_proxy.close()

# Print the count by state
print(state_count)





