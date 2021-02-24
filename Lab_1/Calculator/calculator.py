def sum(m, n):
	result = m
	if n < 0:
		for i in range(abs(n)):
			result -= 1
	else:
		for i in range(n):
			result += 1
	return result

def multiply(m, n):
	result = 0
	for i in range(abs(n)):
		result += m
	if n < 0:
		return -result
	else:
		return result

