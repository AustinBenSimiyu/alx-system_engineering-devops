import requests
def number_of_subscribers(subreddit):
    CLIENT_ID = 'SPa9A7rjRof6kxuWYSA7kA'
    SECRET_KEY = 'L5V5FiyChmjya4jsaxXvJyqBwuF-Yg'
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

    with open('pw.txt', 'r') as f:
        pw = f.read()

    data = {
        'grant_type': 'password',
        'username': 'Fuego_017',
        'password': pw
    }

    headers = {'User-Agent': 'MyAPI/0.0.1'}

    # Get the access token
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

    if res.status_code == 200:
        token = res.json().get('access_token')
        headers['Authorization'] = f'bearer {token}'

        # Now make the request to get the subreddit information
        url = f"https://oauth.reddit.com/r/{subreddit}/about.json"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                subscribers = data['data']['subscribers']
                return subscribers
            else:
                return 0
        else:
            return 0
    else:
        print("Failed to obtain token")
        print(f"Error: {res.status_code}, Response: {res.text}")
