a = 1

for _ in range(100):
	if a % 7 == 0:
		a = a + 1
	elif '7' in str(a):
		a = a + 1
	else:
		print(a)
		a = a + 1
