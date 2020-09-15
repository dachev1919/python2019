import requests

# Creat call API and save response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code:", r.status_code)

# Save the answer API in variable 
response_dict = r.json()

# Processing of result
print(response_dict.keys())