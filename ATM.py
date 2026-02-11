atm_db={
    "name":"Srinu",
    "Account number":1235409687,
    "Phone number":7285962319,
    "Balance":2000,
    "ATM_Pin":"1234",
    "Transaction":[]
}

attempts=3
Pre_balance=atm_db["Balance"]
#ATM PIN VERIFICATION
while attempts>0:
    pin = input("Enter your 4 digit ATM pin: ")
    if pin==atm_db["ATM_Pin"]:
        print("Welcome ",atm_db["name"])
        break
    else:
        attempts=attempts-1
        if attempts>0:
            print("Invalid ATM pin")
            print("Attempts left to enter your correct ATM pin: ",attempts)
        else:
            print("You had entered your ATM pin wrong three times")
            print("ATM card temporarily blocked")

#ATM FEATURES
if pin==atm_db["ATM_Pin"]:
    while True:
        print("**** ATM Menu ****")
        print("\n1.Check Balance \n 2.Deposit Money \n 3.Withdraw Money \n 4.Change Pin number \n 5.Transaction History \n 6.Exit")

        choice=int(input("Enter your choice: "))

#Check Balance
        if choice==1:
            print("Available Balance: ",atm_db["Balance"])

#Deposit Money
        elif choice==2:
            deposit=int(input("Enter deposit amount: "))
            if deposit % 100 ==0:
                atm_db["Balance"]+=deposit
                atm_db["Transaction"].append(deposit)
                print("Amount Successfully deposited")
                print("Available Balance: ",atm_db["Balance"])
            else:
                print("Change can't be deposit. Please deposit multiples of Hundred")

#Withdraw money
        elif choice==3:
            withdraw=int(input("Enter withdraw amount: "))
            if withdraw % 100==0:
                if withdraw<=atm_db["Balance"]:
                    atm_db["Balance"]-=withdraw
                    atm_db["Transaction"].append(-withdraw)
                    print("Amount Successfully withdrawed")
                    print("Remaining Balance: ", atm_db["Balance"])
                else:
                    print("Insufficient Balance")
                    print("You had only",atm_db["Balance"],"in your account")
            else:
                print("Change can't be withdrawn. Please withdraw multiples of Hundred")

#Change Pin number
        elif choice==4:
            enter=input("Enter your old ATM pin: ")
            if enter==atm_db["ATM_Pin"]:
                new=input("Enter your new ATM Pin: ")
                count=0
                for i in new:
                    if i in "1234567890":
                        count+=1
                if count==len(new):
                    if len(new)==4:
                        confirm = input("Confirm your new ATM Pin: ")
                        if new==confirm:
                            atm_db["ATM_Pin"]=new
                            print("New ATM Pin Successfully updated")
                            #print("pin: ",atm_db["ATM_Pin"])
                        else:
                            print("Confirmation pin is not matching with your new pin")
                    elif len(new)<4:
                        print("ATM Pin should contain 4 digits")
                    else:
                        print("ATM Pin should contain 4 digits only")

                else:
                    print("ATM Pin must be in numbers")
            else:
                print("Invalid ATM Pin")

#Transaction History
        elif choice==5:
            if atm_db["Transaction"]==[]:
                print("No transaction history")
            else:
                print("----- Transaction History -----")
                temp_balance=Pre_balance
                print("Previous Balance: ",temp_balance)
                for i in atm_db["Transaction"]:
                    if i >0:
                        temp_balance+=i
                        print("Amount Credited: +",i, " Balance: ",temp_balance)
                    else:
                        temp_balance+= i
                        print("Amount Debited: -",-i, " Balance: ",temp_balance)
                print("Current Balance: ", atm_db["Balance"])

#Exit
        elif choice==6:
            print("Thank you for using our ATM")
            break

        else:
            print("Invalid choice")




