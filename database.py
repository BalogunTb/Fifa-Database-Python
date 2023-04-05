import sqlite3


CREATE_FIFA_TABLE = "CREATE TABLE IF NOT EXISTS fifa (id INTEGER PRIMARY KEY, name TEXT, league TEXT, rating INTEGER);"


INSERT_FIFA = "INSERT INTO fifa (name, league, rating) VALUES (?, ?, ?);" 


GET_ALL_FIFA = "SELECT * FROM fifa;"
GET_FIFA_BY_NAME = "SELECT * FROM fifa WHERE name = ?;"
GET_BEST_TEAM_FOR_FIFA = """
SELECT * FROM fifa
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""

CHECK_FIFA_TABLE = "SELECT name FROM sqlite_master WHERE type='table' AND name='fifa';"

def create_tables(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute(CHECK_FIFA_TABLE)
        result = cursor.fetchone()
        if result:
            # The 'fifa' table already exists
            print("Table 'fifa' already exists.")
        else:
            # Create the 'fifa' table
            cursor.execute(CREATE_FIFA_TABLE)
            print("Table 'fifa' created.")
 

def connect():
 return sqlite3.connect("data.db  ")


def create_tables(connection):
 with connection:
    connection.execute(CREATE_FIFA_TABLE)


def add_fifa(connection, name, league, rating):
  with connection:
    connection.execute(INSERT_FIFA, (name, league, rating))


def get_all_fifa(connection):
  with connection:
    return connection.execute(GET_ALL_FIFA).fetchall()


def get_fifa_by_name(connection, name):
  with connection:
    return connection.execute(GET_FIFA_BY_NAME, (name,)).fetchall()
  
  
def get_best_preparation_for_fifa(connection, name):
  with connection:
    return connection.execute(GET_BEST_TEAM_FOR_FIFA, (name,)).fetchone() 


# create a connection to the database
connection = connect()

# create the 'fifa' table if it doesn't exist
create_tables(connection)

# add a new team to the database
add_fifa(connection, "Real Madrid", "La Liga", 90)

# get all teams in the database
all_teams = get_all_fifa(connection)

# find a team by name
team_by_name = get_fifa_by_name(connection, "Real Madrid")

# find the best team for FIFA by name
best_team = get_best_preparation_for_fifa(connection, "Real Madrid")
