prime_numbers=[]
for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count<=2:
        prime_numbers.append(i)


print(prime_numbers)
