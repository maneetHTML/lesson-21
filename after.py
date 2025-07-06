import requests

def get_random_activity():
    url = "https://www.boredapi.com/api/activity/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Activity: {data['activity']}")
        print(f"Type: {data['type']}")
        print(f"Participants: {data['participants']}")
    else:
        print("Failed to fetch activity.")

get_random_activity()
