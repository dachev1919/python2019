import requests

# Create call Api and save response
url =  'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Save the answer API in variable
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Analyse information about repository
repo_dicts = response_dict['items']
print("Repositorie returned:", len(repo_dicts))

# Analyse first repository
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)

print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at']) 
print('Description:', repo_dict['description'])