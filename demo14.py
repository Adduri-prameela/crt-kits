age=int(input("Enter your age: "))
if(age>=18):
    print("You are eligible to vote.")
else:
    print("You are eligible To vote.")

    #ternary operator
    res="eligible" if age>=18 else "not eligible"
    print("You are",res,"to you.")