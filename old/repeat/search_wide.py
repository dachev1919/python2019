from collections import deque
def person_is_seller(name):
	""""""
	return name[-1] == "m"
	
def search(name):
	""""""
	search_queue = deque()
	search_queue += graph[name]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print(person + " is a mango seller")
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False

if __name__ == "__main__":
	graph = dict()
	graph["Me"] = ["Yarik", "Danya"]
	graph["Yarik"] = ["Anya"]
	graph["Danya"] = ["Rustam"]
	graph["Anya"] = []
	graph["Rustam"] = []
	search("Me") 