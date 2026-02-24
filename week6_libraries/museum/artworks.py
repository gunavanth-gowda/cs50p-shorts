import requests


def get_artworks(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search", {"q": query, "limit": limit}
        )
        response.raise_for_status()
    except requests.HTTPError as err:
        print(err)
        return []

    content = response.json()
    return [artwork["title"] for artwork in content["data"]]
