def is_prime(number):
	count=0
	if number>0:
		for i in range(1, number+1):
			if number%i==0:
				count+=1
		if count>2:
			return True
		else:
			return False 


	else:
		return False



number=int(input("Enter the number: "))
print(is_prime(number))
