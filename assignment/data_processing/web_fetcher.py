import requests

def fetch_user_data(url:str) -> list:
    try:
        res = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"something went wrong. Are you connected to the internet?: {e}")
    else:
        if res.status_code != 200:
            print(f"Failed to fetch data from {url}, status code: {res.status_code}")
            return []
        users = res.json()
        list_of_usernames = []
        for user in users:
            list_of_usernames.append(user["username"])

    return list_of_usernames