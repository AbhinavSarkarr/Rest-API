import requests

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")

# print(response.json()['items'][0]['title'])

for item in response.json()['items']:
    if item['is_answered'] == False:
        print(item['title'])