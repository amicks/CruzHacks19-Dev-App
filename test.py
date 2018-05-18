import requests

endpoint = 'http://localhost:5000/hackers/'

users = [
    {
        "first_name": "Allston",
        "last_name": "Mickey",
        "email": "amicks@github.com",
        "age": 20,
        "needs_transportation": True,
        "shirt_size": "M",
        "university": "UCSC",
    },
    {
        "first_name": "Foo",
        "last_name": "Bar",
        "email": "baz@github.com",
        "age": 18,
        "needs_transportation": False,
        "shirt_size": "S",
        "university": "UCSC",
    },
    {
        "first_name": "X",
        "last_name": "Y",
        "email": "Z@github.com",
        "age": 18,
        "needs_transportation": False,
        "shirt_size": "M",
        "university": "USC",
    },
    {
        "first_name": "A",
        "last_name": "B",
        "email": "C@github.com",
        "age": 21,
        "needs_transportation": True,
        "shirt_size": "M",
        "university": "UCSC",
    }
]

for user in users:
    print(requests.post(endpoint, data=user).json())
