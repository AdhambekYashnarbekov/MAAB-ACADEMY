numbers1 = [1, 1, 2, 3, 4, 2]
numbers2 = [1, 3, 4, 5]
uncommon_list=[]

for number1 in numbers1:
    if number1 not in numbers2:
        uncommon_list.append(number1)

for number2 in numbers2:
    if number2 not in numbers1:
        uncommon_list.append(number2)


print(uncommon_list)


