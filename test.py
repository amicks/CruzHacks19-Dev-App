import requests

endpoint = 'http://localhost:5000/hackers/'

user = {
    "first_name": "Allston",
    "last_name": "Mickey",
    "email": "amicks@github.com",
    "age": 20,
    "needs_transportation": True,
    "shirt_size": "M",
    "university": "UCSC",
}

post_res = requests.post(endpoint, data=user).json()
print(post_res)

get_res = requests.get('{0}?public_id={1}'.format(endpoint, post_res['public_id'])).json()
print(get_res)
