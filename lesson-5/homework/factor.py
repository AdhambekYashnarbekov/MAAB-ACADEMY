
def factor(number):
	results=[]
	for i in range(1, number+1):
		if number%i==0:
			results.append(f"{i} is a factor of {number}")
	return "\n".join(results)



numer=int(input("Enter a positive integer: "))
print(factor(numer))




