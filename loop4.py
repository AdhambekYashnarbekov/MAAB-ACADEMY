import random
count=0
random_number=random.randint(1,100)


while True:
    find_number=int(input("Guess the number: "))
    if find_number>random_number:
        print("Too hight!")
        count+=1
    elif find_number <random_number:
        print("Too low!")
        count+=1
    else:
        print("Congratulations! You find correct number, mind-ninja!")
        break

    
    if count>10:
        print("You tried more than 10 times! Sorry, but you lost the game! ")
        answer=input("Whould you like to start again?\nPossible answers: y, yes, ok, n, no:\n>>> ")
        if answer.lower()=='y' or answer.lower()=='yes' or answer.lower()=='ok':
            continue
        else:
            break


print(random_number)