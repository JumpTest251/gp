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
        data = response.json()
        user_id = data["id"]
        avatar_url = data["avatar_url"]
        
        return (user_id, avatar_url)
    else:
        return None