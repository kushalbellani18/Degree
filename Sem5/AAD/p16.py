class lode:
	def __init__(self, key, value, left=None, right=None):
		self.key = key
		self.value = value
		self.left = left
		self.right = right
		self.code = ''

def calculate_value(data):
	symbols = dict()
	for element in data:
		if symbols.get(element) == None:
			symbols[element] = 1
		else:
			symbols[element] += 1

	return symbols

codes = dict()
def calculate_code(node, val=''):
	newVal = val + str(node.code)

	if(node.left):
		calculate_code(node.left, newVal)
	if(node.right):
		calculate_code(node.right, newVal)

	if(not node.left and not node.right):
		codes[node.key] = newVal

	return codes

def output_encoded(data, coding):
	eC = []
	for c in data:
		print(coding[c], end = '')
		eC.append(coding[c])

	msg = ''.join([str(i) for i in eC])

class point:
	def __init__(self, n):
		self.head = n

	def dis(self, data):
		data += 'x'
		t = self.head
		s = ''

		i = 0
		while(i < len(data)):
			if(t.left == None and t.right == None):
				s += t.key
				t = self.head

			if(data[i] == '0'):
				t = t.left
			else:
				t = t.right

			i += 1

		print(s)

if __name__ == "__main__":
	data = input("Enter data: ")
	#dataDict = calculate_value(data)

	dataDict = {'A':0.5, 'B':0.35, 'C':0.5, 'D':0.1, 'E':0.4, '-':0.2}

	keys = dataDict.keys()
	values = dataDict.values()

	print("Key: ", keys)
	print("Value: ", values)

	nodes = []

	for key in keys:
		nodes.append(lode(key, dataDict.get(key)))

	while len(nodes) > 1:
		nodes = sorted(nodes, key=lambda x:x.value)

		right = nodes[0]
		left = nodes[1]

		left.code = 0
		right.code = 1

		nodes.remove(left)
		nodes.remove(right)
		nodes.append(lode(key=left.key+right.key, value=left.value+right.value, left=left, right=right))

	encoding = calculate_code(nodes[0])
	print(encoding)
	print("<->")
	output_encoded(data, encoding)

	print("")

	p = point(nodes[0])
	p.dis('1100100011100011')
	p.dis('11')
