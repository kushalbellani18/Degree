import sys

if __name__ == "__main__":
	txt = sys.argv[1]
	txt_backup = sys.argv[1]

	d = dict()

	ri = 1
	for t in txt:
		if t not in ['+', '-', '*', '/', "="] and t not in d:
			d[t] = str(ri)
			ri += 1

	query = []
	for op in ["/", "*", "+", "-"]:
		i = 0
		while i < len(txt):
			if txt[i] == op:
				before_i = txt[i-1]
				after_i = txt[i+1]

				query.append("MOV " + d[before_i] + ", " + before_i)
				query.append("MOV " + d[after_i] + ", " + after_i)

				d[d[before_i]] = str(ri)
				ri += 1

				txt = txt.replace(before_i+txt[i]+after_i, d[before_i])

				if op == '/':
					query.append("DIV " + d[before_i] + ", " + d[after_i])
				elif op == '*':
					query.append("MUL " + d[before_i] + ", " + d[after_i])
				elif op == '+':
					query.append("ADD " + d[before_i] + ", " + d[after_i])
				elif op == '-':
					query.append("SUB " + d[before_i] + ", " + d[after_i])

			i += 1

	query.append("MOV " + txt[0] + ", " + txt[-1])

	for i in range(0, len(query)):
		qi = 0
		while(qi < len(query[i])):
			if query[i][qi] in [str(a) for a in range(0, 10)]:
				query[i] = query[i].replace(query[i][qi], "R"+query[i][qi])

				qi += 1

			qi += 1

	for q in query:
		print(q)
