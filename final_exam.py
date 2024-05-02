class bank:
    total_balance = 0
    total_loan = 0
    loan_status = False
    account_list = []
    admin = False
    account_number_counter = 1000
    def update_account_list(self,account):
        self.account_list.append(account)
class admin(bank):
    def login_as_admin(self, name, password):
        if not self.admin:
            print("NO ADMIN EXISTS")
            return False
        else:
            if bank.admin['name'] == name and bank.admin['password'] == password:
                print('\nADMIN LOGGED IN SUCCESSFULLY !!!\n')
                return True
            else:
                print('INVALID USER NAME OR PASSWORD')
                return False

    def reg_as_admin(self,name,password):
        if bank.admin != False:
            print('ADMIN ALREADY EXISTS')
        else:
            bank.admin = {'name':name,'password': password}
            print('\nAN ADMIN REGISTERED SUCCESSFULLY !!!\n')

    def check_balance(self):
        print(f'TOTAL AVAILABLE BALANCE OF THE BANK : {self.total_balance}\n')

    def check_loan_balance(self):
        print(f'TOTAL AMOUNT OF LOAN TAKEN FROM THE BANK : {self.total_loan}\n')

    def switching_loan_status(self):
        if bank.loan_status == True:
            bank.loan_status = False
            print('\nLOAN STATUS CHANGE TO OFF\n')
        elif bank.loan_status == False:
            bank.loan_status = True
            print('\nLOAN STATUS CHANGE TO ON\n')


    def show_users(self):
        print("************************************************* USER LISTS *************************************************")
        print('ACCOUNT_NUMBER\t\tACCOUNT_HOLDER\t\t\tACCOUNT_TYPE\t\t BALANCE\t\t LOAN AMOUNT\t\t LOAN TAKEN\n')
        for x in self.account_list:
            print(x['account_number']+'\t\t\t\t'+x['name']+'\t\t\t\t\t'+x['account_type']+'\t\t\t\t',x['balance'],'\t\t\t\t',x['loan_amount'],'\t\t\t\t\t',x['loan_taken'])

    def delete_account(self,account_number):
        for x in self.account_list:
            if(x['account_number'] == str(account_number)):
                self.account_list.remove(x)

    def check_loan_status(self):
        if(self.loan_status == True):
            print('LOAN STATUS : ON\n')
        elif(self.loan_status == False):
            print('LOAN STATUS : OFF\n')



class users(bank):
    transaction_list = []
    def create_account(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type

        self.account_number = self.account_number_counter
        self.account_number_counter = self.account_number_counter + 1

        account = {'account_number': str(self.account_number), 'name': name, 'email': email,'address': address, 'account_type': account_type,'balance': 0,'loan_amount': 0,'loan_taken' : 0}
        self.account_list.append(account)
        print(f'CONGRATULATIONS !!! YOUR ACCOUNT HAS BEEN CREATED \nYOUR ACCOUNT NUMBER IS {account["account_number"]}\n')

    def deposit(self,amount,account_number):
        for x in self.account_list:
            if(x['account_number'] == account_number):
                x['balance'] = x['balance'] + amount
                bank.total_balance = bank.total_balance + amount
                transaction = {'account_number': account_number, 'balance': amount, 'transaction_type': 'deposit'}
                self.transaction_list.append(transaction)
                print(f'\n{amount} TAKA IS DEPOSITED SUCCESSFULLY !!!\n')

    def withdraw(self,amount,account_number):
        for x in bank.account_list:
            if(x['account_number'] == account_number):
                if(x['balance']>self.total_balance):
                    print('YOU CAN NOT WITHDRAW FUNDS. THE BANK IS BANKRUPT')
                else:
                    if (x['balance'] > amount):
                        x['balance'] = x['balance'] - amount
                        bank.total_balance = bank.total_balance - amount
                        transaction = {'account_number': account_number, 'balance': -amount,
                                       'transaction_type': 'withdraw'}
                        self.transaction_list.append(transaction)
                        print(f'\n{amount} TAKA IS WITHDRAWN SUCCESSFULLY !!!\n')
                    else:
                        print('WITHDRAWAL AMOUNT EXCEEDED')

    def transaction_history(self, account_number):
        is_transaction_made = 0
        for x in self.account_list:
            if(x['account_number']==account_number):
                    print()
                    for x in self.transaction_list:
                        if (x['account_number'] == account_number):
                            is_transaction_made += 1
                            if 'balance' and 'transaction_type' in x:
                                if x['balance'] < 0:
                                    if x['transaction_type'] == 'withdraw':
                                        print(f'YOU WITHDRAWN\t{-x["balance"]} TAKA')
                                    elif x['transaction_type'] == 'transfer' and 'receiver' in x:
                                        print(f'YOU SENT {-x["balance"]} TAKA TO ACCOUNT NUMBER {x["receiver"]}')

                                elif x['balance'] > 0:
                                    if x['transaction_type'] == 'deposit':
                                        print(f'YOU DEPOSITED\t{x["balance"]} TAKA')
                                    elif x['transaction_type'] == 'transfer' and 'sender' in x:
                                        print(f'YOU RECEIVED {x["balance"]} TAKA FROM ACCOUNT NUMBER {x["sender"]}')
                            elif 'loan_amount' in x:
                                if x['loan_amount'] > 0:
                                    print(f'YOU TOOK LOAN\t{x["loan_amount"]} TAKA')
                                elif x['loan_amount'] < 0:
                                    print(f'YOU REPAY LOAN\t{-x["loan_amount"]} TAKA ')


        if is_transaction_made == 0:
            print('YOU DID NOT MAKE ANY TRANSACTION')
        else:
            for x in self.account_list:
                if x['account_number'] == account_number:
                    a = x.get('balance', 0)
                    print(f'\nYOUR CURRENT BALANCE :  {a}\n')

    def taking_loan(self,account_number,amount):
        if not self.loan_status:
            print('\nYOU CAN NOT TAKE LOAN AT THIS MOMENT. PLEASE TRY AGAIN LATER\n')
        else:
            for x in self.account_list:
                if (x['account_number'] == account_number):
                    if (amount > self.total_balance):
                        print('YOU CAN NOT TAKE LOAN. THE BANK IS BANKRUPT')
                    elif (x['loan_taken'] < 2):
                        x['loan_amount'] = x['loan_amount'] + amount
                        bank.total_loan = bank.total_loan + amount
                        bank.total_balance = bank.total_balance - amount
                        transaction = {'account_number': account_number, 'loan_amount': amount}
                        self.transaction_list.append(transaction)
                        x['loan_taken'] = x['loan_taken'] + 1
                        print(f'\n{amount} TAKA LOAN TAKEN FROM THE BANK SUCCESSFULLY !!!\n')
                    else:
                        print('\nYOU CAN TAKE LOAN FROM THE BANK AT MOST TWO TIMES\n')
                        break

    def repay_loan(self,account_number,amount):
        for x in self.account_list:
            if(x['account_number'] == account_number):
                if(x['loan_taken'] > 0):
                    x['loan_amount'] = x['loan_amount'] - amount
                    x['loan_taken'] = x['loan_taken'] - 1
                    bank.total_loan = bank.total_loan - amount
                    bank.total_balance = bank.total_balance + amount
                    transaction = {'account_number': account_number, 'loan_amount': amount}
                    self.transaction_list.append(transaction)
                    print(f'SUCCESSFULLY REPAY  {amount} TAKA LOAN')
                else:
                    print('YOU DID NOT TAKE ANY LOAN YET')

    def check_balance(self,account_number):
        for x in self.account_list:
            if(x['account_number'] == account_number):
                print(f'\nYOUR AVAILABLE BALANCE IS : {x["balance"]} TAKA\n')
                break
            else:
                continue

    def transfer_balance(self,sender_account_number,receiver_account_number,amount):
        current_balance_of_sender = 0
        for x in self.account_list:
            if(x['account_number']==sender_account_number):
                if(x['balance'] > amount):
                    x['balance'] = x['balance'] - amount
                    current_balance_of_sender = x['balance']
                    transaction = {'account_number': sender_account_number, 'balance': -amount, 'transaction_type': 'transfer', 'sender': sender_account_number, 'receiver': receiver_account_number}
                    self.transaction_list.append(transaction)

                else:
                    print('YOU DON\'T HAVE ENOUGH MONEY TO TRANSFER')
                    return
        for x in self.account_list:
            if (x['account_number'] == receiver_account_number):
                x['balance'] = x['balance'] + amount
                transaction = {'account_number': receiver_account_number, 'balance': amount, 'transaction_type': 'transfer','sender': sender_account_number, 'receiver': receiver_account_number}
                self.transaction_list.append(transaction)
                print(f'SEND {amount} TAKA TO ACCOUNT NUMBER {receiver_account_number} IS SUCCESSFUL')

        print(f'YOUR CURRENT BALANCE IS : {current_balance_of_sender} TAKA')

    def check_user_exists(self,account_number):
        exists = 0
        for x in self.account_list:
            if(x['account_nubmer'] == account_number):
                exists += 1
        return 0

    def account_number_check(self,account_number):
        for x in self.account_list:
            if(x['account_number'] == account_number):
                return True

        return False
    def user_login(self,account_number,name):
        for x in self.account_list:
            if(x['account_number']==account_number):
                if(x['name'] == name):
                    return True
                else:
                    print(f'{name} IS NOT CONNECTED WITH ACCOUNT NUMBER {account_number}')
                    return False
        print(f'ACCOUNT NUMBER {account_number} DOES NOT EXISTS. PLEASE CREATE AN ACCOUNT')
        return False


my_bank = bank()
bank_admin =  admin()
bank_user =  users()
print('---------------------------------------------------WELCOME TO AJ ACHE KAL NEI BANK---------------------------------------------------')
# bank_user.create_account('zayed','zayed@gmail.com','dhaka','SAVINGS')
# bank_user.create_account('abul','abul@gmail.com','ctg','SAVINGS')
# bank_user.create_account('kabul','kabul@gmail.com','rangpur','SAVINGS')
# bank_user.create_account('sabul','sabul@gmail.com','sylhet','SAVINGS')
# bank_admin.show_users()
main_menu = True
while main_menu:
    print('1. ADMIN')
    print('2. USER')
    print('3. EXIT')
    option = int(input('CHOOSE A OPTION : '))
    if(option == 1):
        print('1. LOG IN')
        print('2. REGISTRATION')
        print('3. MAIN MENU')
        print('4. EXIT')
        op = int(input('CHOOSE A OPTION : '))
        if(op==1):
            name = input("ENTER NAME : ")
            password = input("ENTER PASSWORD : ")
            check_status = bank_admin.login_as_admin(name,password)
            print()
            if(check_status == True):
                print(f'\n!!!-----------------------------------------------WELCOME ADMIN -----------------------------------------------!!!\n')
                while True:
                    print('1. DELETE A USER ACCOUNT ')
                    print('2. SHOW ALL USER ACCOUNTS LIST ')
                    print('3. TOTAL AVAILABLE BALANCE OF THE BANK ')
                    print('4. TOTAL LOAN GIVEN ')
                    print('5. LOAN STATUS OF THE BANK ')
                    print('6. CHANGE LOAN STATUS ')
                    print('7. MAIN MENU ')
                    print('8. EXIT ')

                    x = int(input('CHOOSE A OPTION  : '))
                    if (x == 1):
                        account_number = int(input("ENTER ACCOUNT NUMBER : "))
                        bank_admin.delete_account(account_number)
                        print()
                        print(f'\nACCOUNT NUMBER {account_number} HAS BEEN DELETED FROM THE DATABASE\n')
                    elif (x == 2):
                        print()
                        bank_admin.show_users()

                    elif (x == 3):
                        print()
                        bank_admin.check_balance()
                    elif (x == 4):
                        print()
                        bank_admin.check_loan_balance()
                    elif (x == 5):
                        print()
                        bank_admin.check_loan_status()
                    elif(x == 6):
                        bank_admin.switching_loan_status()
                    elif (x == 7):
                        break
                    elif (x == 8):
                        main_menu = False
                        break

        elif(op==2):
            name = input("ENTER NAME : ")
            password = input("ENTER PASSWORD : ")
            bank_admin.reg_as_admin(name, password)
        elif(op == 3):
            continue
        elif(op == 4):
            break
        else:
            print('\nINVALID INPUT\n')

    elif(option == 2):
        user_menu = True
        while user_menu:
            print('1. I HAVE AN ACCOUNT ALREADY')
            print('2. I WANT TO CREATE AN ACCOUNT')
            print('3. MAIN MENU')
            print('4. EXIT')
            op = int(input('CHOOSE A OPTION : '))
            if(op==1):
                account_number = input('ENTER YOUR ACCOUNT NUMBER : ')
                name = input('ENTER YOUR ACCOUNT NAME : ')
                check_user = bank_user.user_login(account_number,name)
                if(check_user == True):
                    while True:
                        print(f'\n!!!-----------------------------------------------WELCOME {name} -----------------------------------------------!!!\n')
                        print('1. WITHDRAW FUNDS')
                        print('2. DEPOSIT FUNDS')
                        print('3. CHECK AVAILABLE BALANCE')
                        print('4. TRANSACTION HISTORY')
                        print('5. TAKE LOAN')
                        print('6. REPAY LOAN')
                        print('7. TRANSFER MONEY TO ANOTHER ACCOUNT')
                        print('8. USER MENU')
                        print('9. MAIN MENU')
                        print('10. EXIT')
                        x = int(input("CHOOSE A OPTION : "))

                        if (x == 1):
                            amount = int(input('ENTER AMOUNT : '))
                            bank_user.withdraw(amount, account_number)
                        elif (x == 2):
                            amount = int(input('ENTER AMOUNT : '))
                            bank_user.deposit(amount, account_number)
                        elif (x == 3):
                            bank_user.check_balance(account_number)
                        elif (x == 4):
                            bank_user.transaction_history(account_number)

                        elif (x == 5):
                            amount = int(input('ENTER AMOUNT : '))
                            bank_user.taking_loan(account_number, amount)

                        elif (x == 6):
                            amount = int(input('ENTER AMOUNT : '))
                            account_number = input('ENTER ACCOUNT NUMBER : ')
                            bank_user.repay_loan(account_number, amount)

                        elif (x == 7):
                            while True:
                                sender_account_number = account_number
                                sender_account_checker = bank_user.account_number_check(sender_account_number)
                                if (sender_account_checker == False):
                                    print('WRONG ACCOUNT NUMBER ENTERED')
                                    continue
                                else:
                                    receiver_account_number = input('ENTER RECEIVER ACCOUNT NUMBER : ')
                                    receiver_account_checker = bank_user.account_number_check(receiver_account_number)
                                    if (receiver_account_checker == False):
                                        print('WRONG ACCOUNT NUMBER ENTERED')
                                        continue
                                    else:
                                        amount = int(input('ENTER AMOUNT : '))
                                        bank_user.transfer_balance(sender_account_number, receiver_account_number, amount)
                                        break

                        elif (x == 8):
                            break
                        elif (x == 9):
                            user_menu = False
                            break
                        elif (x == 10):
                            user_menu = False
                            main_menu = False
                            break
                        else:
                            print('\nINVALID INPUT\n')
                else:
                    break
            elif(op==2):
                name = input('ENTER YOUR NAME : ')
                email = input('ENTER YOUR EMAIL : ')
                address = input('ENTER YOUR ADDRESS : ')
                while True:
                    account_type = input('ENTER YOUR ACCOUNT TYPE SAVINGS OR CURRENT : ')
                    if (account_type.upper() == 'SAVINGS' or account_type.upper() == 'CURRENT'):
                        break
                    else:
                        print('INVALID ACCOUNT TYPE')

                bank_user.create_account(name, email, address, account_type)
                break
            elif(op==3):
                break
            elif(op==4):
                main_menu = False
                break
            else:
                print('\nINVALID INPUT\n')
    elif(option == 3):
        break
    else:
        print('\nINVALID INPUT\n')