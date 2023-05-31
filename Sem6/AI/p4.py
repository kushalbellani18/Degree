import pandas as pd
import math
import gmplot

def getMapInfo():
	f = open("file/map.txt", 'r')

	d = {}

	for x in f:
		if(x[0] == "-"):
			k = x[1:-1]
			d[k] = []
		else:
			x = x[:-1]
			s = x.split(',')
			s[1] = float(s[1])

			d[k].append(s)

	f.close()

	return d

def getLocationInfo(map):
	location = {}
	df = pd.read_csv("file/IndiaCitiesLatLng.csv")

	for x,y in map.items():
		location[x] = {
			"next": y,
			"lat": df[df["city"].str.lower() == x]['lat'].values[0],
			"log": df[df["city"].str.lower() == x]['lng'].values[0],
			"heuristic": None
		}

	return location

# For Heuristic function
def getHeuristic(location, goal):
	df = pd.read_csv("file/CitiesHn.csv")

	for x, y in location.items():
		location[x]["heuristic"] = df[df["Goal"] == goal.capitalize()][x.capitalize()].values[0]

	#print(location)
	return location

def disMap(location, p):
	lat_list = []
	lng_list = []

	for i in p:
		lat_list.append(location[i]["lat"])
		lng_list.append(location[i]["log"])

	lol = gmplot.GoogleMapPlotter(sum(lat_list)/len(lat_list), sum(lng_list)/len(lng_list), 13)

	lol.scatter(lat_list, lng_list, 'red', size=40, marker="*")
	lol.plot(lat_list, lng_list, 'blue', edge_width=2.5)

	lol.draw("lol.html")

def aStarAlgo(location, inital, goal):
	visited = []
	path = {
		0: {"curr": [inital], "cost": 0}
	}
	# current = inital
	visited.append(inital)
	d = 0

	while(True):
		d += 1
		current = path[len(path)-1]["curr"][-1]

		#print("+====================+")
		#print(current)

		if(current == goal):
			print("Found")

			print(path[len(path)-1]["curr"])

			disMap(location, path[len(path)-1]["curr"])

			break

		arr = []
		for i in range(0, len(location[current]['next'])):
			gCity = location[current]['next'][i][0]
			gN = location[current]['next'][i][1]
			cost = path[len(path)-1]["cost"]

			#print(str(cost) + " + " + str(gN) + " + " + str(location[gCity]['heuristic'] * d) + " << " + gCity + " >> ")
			if(gCity not in visited):
				arr.append([cost + gN + (location[gCity]['heuristic']), [gCity, gN]])

		if(len(arr) == 0):
			print("Failed!")
			break

		minValue = min(arr)
		#print(minValue)
		# index = -1
		for i in range(0, len(path)):
			if(path[i]["curr"][-1] == current):
				path[i]["curr"].append(minValue[-1][0])
				path[i]["cost"] += minValue[-1][1]

				visited.append(minValue[-1][0])

				break

		#print("+====================+")


if __name__ == "__main__":
	distance = {}
	location = {}

	distance = getMapInfo()
	location = getLocationInfo(distance)

	inital = input("Enter initial city: ").lower()
	goal = input("Enter goal city: ").lower()

	location = getHeuristic(location, goal)

	aStarAlgo(location, inital, goal)

	print(location)

