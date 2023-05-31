import sys

if __name__ == "__main__":
	txt = sys.argv[1]

	d = dict()

	ri = 1
	for t in txt:
		if t not in ['+', '-', '/', '*', '='] and t not in d:
			d[t] = str(ri)
			ri += 1

	#print(d)
	query = []
	for op in ['/', '*', '+', '-']:
		i = 0
		while(i < len(txt)):
			if txt[i] == op:
				before_i = txt[i-1]
				after_i = txt[i+1]

				query.append("MOV " + d[before_i] + ", " + before_i)
				query.append("MOV " + d[after_i] + ", " + after_i)

				d[d[before_i]] = str(ri)
				ri += 1

				if txt[i] == '/':
					query.append("DIV " + d[before_i] + ", " +d[after_i])
				elif txt[i] == '*':
					query.append("MUL " + d[before_i] + ", " +d[after_i])
				elif txt[i] == '+':
					query.append("ADD " + d[before_i] + ", " +d[after_i])
				elif txt[i] == '-':
					query.append("SUB " + d[before_i] + ", " +d[after_i])

				txt = txt.replace(before_i + txt[i] + after_i, d[before_i])

				i = -1

			i += 1

	query.append("MOV " + txt[0] + ", " + txt[-1])

	for i in range(0, len(query)):

		j = 0
		while(j < len(query[i])):
			if query[i][j].isdigit():
				query[i] = query[i].replace(query[i][j], "R"+query[i][j])
				j += 1

			j += 1

	for q in query:
		print(q)
