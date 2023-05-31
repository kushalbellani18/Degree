import gmplot

lat_list = [30, 30.204, 30.35]
lng_list = [77.88, 78, 78.13]

lol = gmplot.GoogleMapPlotter(30.31, 78.032, 13)

lol.scatter(lat_list, lng_list, '#FF0000', size=40, marker=False)

lol.plot(lat_list, lng_list, 'cornflowerblue', edge_width=2.5)

lol.draw("lol.html")
