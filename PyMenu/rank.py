import requests



URL = "https://kienkiddo.dev/ranking.php"

def get_ranking():
    return requests.get(URL, {"action": "view"}).json()

def insert_ranking(name, score):
    return requests.post(URL + "?action=insert", data = {"name": name, "score": score})

