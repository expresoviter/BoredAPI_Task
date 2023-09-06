# Test task with the usage of Bored API
## API Calls
The API Wrapper is created in file [wrapper.py](wrapper.py). Create an object of APIWrapper() and use 'request' method
to get a random activity or an activity with specified parameters. 
You have to pass parameters to this method as a dictionary (ex. `APIWrapper().request({"type" : "education"})`).
The method returns a random activity.

## Database
In the task I use PostgreSQL and SQLAlchemy ORM. 
Classes of interaction with the database are created in file [database.py](database.py).
Connection details are specified in file [configuration.py](configuration.py).
ActivitySaver class have 'saveActivity' method that takes the returned activity as a parameter and saves it to the DB.
The 'getLatestActivities' method makes a query that returns last 5 records from the table.

## Command Line Program
In this task I used 'argparse' module. The program is created in file [my_program.py](my_program.py).
The command of getting a random activity looks like this:

`python my_program.py new --type education --participants 1 --minprice 0.1 --maxprice 30 --minaccessibility 0.1 --maxaccessibility 0.5`

The command of getting last 5 saved activities looks like this:

`python my_program.py list`

