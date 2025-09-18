print("WELCOME to BARODA Bank service!")
print("Insert Debit or Credit Card")
card_status = int(input("Press 1.proceed 0.stop:"))
balance = 77777
user_pin = 143143
if card_status:
    option = int(input("Press 1.Balance Enquiry  2.Withdrawal  3.Deposit:"))
    if option in (1,2,3) :
        bank_type = int(input("Press 1.Savings Account 2.Current Account:"))
        if bank_type in (1,2) :
            pin =int(input("Enter your Pin!:"))
            if pin==user_pin:
                if option ==1:
                    print(f"Current Balance is {balance}")
                elif option==2:
                    withdraw_amount = int(input("Enter amount multiples of 100 to Withdraw:"))
                    if withdraw_amount % 100 == 0:
                        if withdraw_amount<=balance:
                            if withdraw_amount <50000:
                                balance -= withdraw_amount
                                print("Transaction Completed!")
                                print("Please collect Your Cash!")
                                print("Do you want View Your Balance")
                                view = int(input("Press 1.Display balance 0.Exit:"))
                                if view:
                                    print(f"Updated Balance is {balance}")
                                else:
                                    print("thanks for Visiting!")
                            else:
                                print("You can only Withdraw amount each time  upto 50000")
                        else:
                            print("Insufficient  Balance")
                    else:
                        print("Invalid Amount(Can be Multiple of 100)")
                elif option==3:
                    pass
                    deposit = int(input("Enter Amount to Deposit:"))
                    balance += deposit
                    print("Amount Deposited Successfully")
                    print(f"updated balance is {balance}")
                else:
                    print("Invalid option selected")
            else:
                print("Wrong Pin!")
        else:
            print("Invalid Account Type")
    else:
        print("Invalid Option")
else:
    print("Thanks! for Visiting")