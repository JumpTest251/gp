import requests

def fetch_github_user(username):
    """
    Fetches the user id and avatar_url of a given GitHub username using the GitHub API.

    :param username: GitHub username
    :return: User ID if found, else None
    """
    url = 'https://api.github.com/users/' + username
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
