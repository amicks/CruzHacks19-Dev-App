# CruzHacks19-Dev-App
First install dependencies:

``` bash
pip3 install -r requirements.txt
```

Then export your SQL database URI as an environment variable for Flask SQLAlchemy hooks.
The following are examples for MySQL, Postgres, and SQLite:

``` bash
export SQLALCHEMY_DATABASE_URI='mysql+pymysql://user:password@localhost:port/db_name'
export SQLALCHEMY_DATABASE_URI='postgresql://user:password@localhost:port/db_name'
export SQLALCHEMY_DATABASE_URI='sqlite:////path/db_name.db'
```

Start the Flask Server:

``` bash
python3 ./src/app.py
```

You can now GET, POST, PUT, or DELETE from the Hacker DB model on the route `http://localhost:5000/hackers/`
Read ./src/api.py for arguments and types that each type of request accepts.  In general, everything except GET requires a `public_id` integer.  GET can filter the DB model on any categories.

There is a test.py file that POSTs 5 users and prints the response if you want to run it in another shell.
Or POST manually (the following arguments are *required* for any POST, there are more optional ones in the source code):

``` bash
curl -H "Content-Type: application/json" -d '{"age": 20, "email": "amicks@github.com", "first_name": "Allston", "last_name": "Mickey", "shirt_size": "M", "needs_transportation": true}' http://localhost:5000/hackers/
```

Response:

``` bash
{
    "public_id": 6629,
    "team_id": null,
    "first_name": "Allston",
    "last_name": "Mickey",
    "email": "amicks@github.com",
    "gender": null,
    "age": 20,
    "needs_transportation": true,
    "rsvp_status": null,
    "app_status": null,
    "shirt_size": "M",
    "university": null,
    "class_year": null
}
```
