
while True:
    password=input("Enter a password:\n>>> ")
    if len(password)<8:
        print("Password is too short!")
        continue
    else:
        count=0
        for char in password:

            if char>="A" and char<="Z":
                count+=1
            
        if count>0:
            print("Password is strong!")
            break
        else:
            print("Password must contain an uppercase letter.")


        

        


     

    
    
    




    


    

    

    