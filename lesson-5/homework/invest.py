import math
def invest(amount, rate, year):
	results=[]
	for i in range(1,year+1):
		total=amount*pow(1+rate,i)
		results.append(f"year {i}: ${total:.2f}")
	return "\n".join(results)


amount=float(input("Input the starting amount: "))
rate=float(input("What is the rate of benefit: "))
year=int(input("How many years you want to ivnest: "))


print(invest(amount, rate, year))

