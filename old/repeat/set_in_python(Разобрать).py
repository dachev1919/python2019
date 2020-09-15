if __name__ == "__main__":
	states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
	stations = {}
	stations["first"] = set(["id", "nv", "ut"])
	stations["second"] = set(["wa", "id", "mt"])
	stations["third"] = set(["or", "nv", "ca"])
	stations["fours"] = set(["nv", "ut"])
	stations["fifth"] = set(["ca", "az"])
	final_stations = set()
	while states_needed:
		print('while')
		best_station = None
		states_covered = set()
		for station, states in stations.items():
			print("for")
			covered = states_needed & states
			if len(covered) > len(states_covered):
				best_station = station
				states_covered = covered
		states_needed -= states_covered
		final_stations.add(best_station)
	print(final_stations)