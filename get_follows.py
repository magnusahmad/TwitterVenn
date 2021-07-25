import os
import pandas as pd
import json
import requests
import sys

#def auth():
 #   return os.environ.get("YOUR_BEARER_TOKEN")

def create_url_f(user_id):
    return "https://api.twitter.com/2/users/{}/following?&max_results=1000".format(user_id)

def get_params_f():
    return {"user.fields": "created_at"}

def create_headers_f(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint_f(url, headers, params):
    response = requests.request("GET", url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request retur133ned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

#only works if the user is discoverable
def main_f(user_id):
    dictionary_of_follows = {}
    for user in user_id:
        bearer_token = 'YOUR_BEARER_TOKEN'
        url = create_url_f(user)
        headers = create_headers_f(bearer_token)
        params = get_params_f()
        json_response = connect_to_endpoint_f(url, headers, params)
        json_file = json.loads((json.dumps(json_response, indent=4, sort_keys=True)))
        try:
            df = pd.json_normalize(json_file['data'])
        except LookupError:
            print (f'Error: Profile of user {user} is set to private mode')
            break
        else:
            filename = '%s.csv' % user
            df.to_csv(filename)
            print(str(user))
    return 'done'
