import requests
import os
import json

#def define_user():
#    user_list = []
#    user1 = input('Enter first user')
#    user2 = input('Enter second user')
#    user_list.append(user1)
#    user_list.append(user2)
#    return user_list

def create_url_u(user1, user2):
    usernames = 'usernames={},{}'.format(user1, user2)
    user_fields = "user.fields=id"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


def create_headers_u(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint_u(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def get_user_ids_u(user_list):
    while True:
        user1 = user_list[0]
        user2 = user_list[1]
        print(user1, user2)
        bearer_token = '{YOUR BEARER TOKEN}'
        url = create_url_u(user1, user2)
        headers = create_headers_u(bearer_token)
        user_ids = []
        json_response = connect_to_endpoint_u(url, headers)
        json_file = json.loads((json.dumps(json_response, indent=4, sort_keys=True)))
        try:
            df = pd.json_normalize(json_file['data'])
        except LookupError:
            print(json_file['errors'])
            print('Looks like one of those users does not exist. Please try again')
        else:
            user_ids = list(df['id'])
            user_set = dict.fromkeys(user_list)
            user_set[user_list[0]] = user_ids[0]
            user_set[user_list[1]] = user_ids[1]
            break

    return user_set
