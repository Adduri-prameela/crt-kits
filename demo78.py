pin=int(input("Enetr the pin: "))
acc_bal=0
if pin==1234:
    print("welcome to the bank")
# Deposit, Withdrawal, Balance Enquiry and Exit.
    while True:
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Balance Enquiry")
        print("4. Exit")

        choice=int(input("Enter YOur Choice :")) 
        print("\n")
        if(choice==1):
            amount=int(input("Enter amount to deposit :"))
            acc_bal=acc_bal+amount
            print(f"Dear Customer your account xxxxxxxxxx1234 is credited with {amount}")
        elif(choice==2):
            amount=int(input("Enter the amount to Withdraw :"))
            if(amount<acc_bal):
                print(f"Dear Customer your account xxxxxxxxxx1234 is debited with {amount}")    
                acc_bal=acc_bal-amount
            else:
                print("Insufficient balance....!")
        elif(choice==3):
             print(f"Dear Customer your account xxxxxxxxxx1234 has with {acc_bal} .")  
        else:
             print("Thank you......!")
             break
else:
    print("You Entered Wrong pin.")
