import requests

def fetch_github_user(username):
    """
    Fetches the user id and avatar_url of a given GitHub username using the GitHub API.

    :param username: GitHub username
    :return: User ID if found, else None
    """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('id'), user_data.get('avatar_url')
    else:
        print(f"Error: Unable to fetch user data. Status Code: {response.status_code}")
        return None