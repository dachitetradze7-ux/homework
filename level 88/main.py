def ATM():
    balance = 1000
    tranasactions = []

    while True:
        print("1. main menu")
        print("2. check balance")
        print("3. withdraw")
        print("4. last 5 tranactions")
        print("5. Exit the ATM")

        choice = input("choose operation (1-5): ")

        try:
            if choice == "1":
                print(f"your balance: {balance} gel")
            elif choice == "2":
                amount = float(input("amount of payment: "))
                if amount <= 0:
                    print("invalid: cash must be possitive!")
                else:
                    balance += amount
                    tranasactions.append({"type": tranasactions, "amount": amount, "balance": balance})
                    print(f"cash succesfuly added {balance}")
            elif choice == "3":
                amount = float(input("withdraw: "))
                if amount <= 0:
                    print("invalid: cash must be possitive!")
                elif amount > balance:
                    print("invalid: there is not enough cash!")
                else:
                    balance -= amount
                    tranasactions.append({"type": tranasactions, "amount": amount, "balance": balance})
                    print(f"succsefuly payment {balance}")
            elif choice == "4":
                print("last 5 transactions")
                for t in tranasactions[-5:]:
                    print(f"type: {t["type"]}, cash: {t["amount"]}, balance: {t["balance"]}")
                if not tranasactions:
                    print("no transactions!")
            elif choice == "5":
                print(f"balance: {balance}")
                print(f"history of transactions: {len(tranasactions)}")
                print("aba he kide gvewvie da gagvamdidre🚨")
                

            else:
                print("invalid: please choose number from-1 to-5!")
        except ValueError:
            print("invalid: please enter valid number!")
ATM()
                        

            
                                




    

   