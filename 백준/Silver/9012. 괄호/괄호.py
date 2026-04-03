T = int(input())

for _ in range(T):
	stack = []
	vps = list(input())
	result = 1
	for v in vps:
		if v == ')':
			try:
				output = stack.pop()
				if output != '(':
					result = 0
					break
			except IndexError:
				result = 0
				break
		elif v == '(':
			stack.append('(')
	if len(stack) != 0:
		result = 0
	if result == 0:
		print("NO")
	else:
		print("YES")