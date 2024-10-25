import datetime  # Importing datetime module for handling time
import sys  # Importing sys module to handle system exit

class ATM:
    def __init__(self):
        # Initializing balance and transaction history
        self.balance = 0.0  # 存储余额 (Store balance)
        self.history = []  # 存储交易历史记录 (Store transaction history)

    def check_balance(self):
        # Function to display balance
        print(f"您的当前余额是: ¥{self.balance}")  # Show current balance
        print(f"查询时间：{datetime.datetime.now()}")  # Show current time

    def deposit(self, amount):
        # Function to deposit money
        if amount > 0:
            self.balance += amount  # Add amount to balance
            print(f"成功存入: ¥{amount}")  # Display deposit success
            self.history.append((datetime.datetime.now(), "存款", amount))  # Record transaction
        else:
            print("存款金额必须大于0")  # Display error if amount <= 0

    def withdraw(self, amount):
        # Function to withdraw money
        if amount > self.balance:
            print("余额不足，无法取款")  # Display insufficient funds error
        elif amount <= 0:
            print("取款金额必须大于0")  # Display error if amount <= 0
        else:
            self.balance -= amount  # Subtract amount from balance
            print(f"成功取出: ¥{amount}")  # Display withdrawal success
            self.history.append((datetime.datetime.now(), "取款", -amount))  # Record transaction

    def show_history(self):
        # Function to display transaction history
        print("您的交易记录如下：")  # Display transaction history header
        for transaction in self.history:
            print(f"时间: {transaction[0]}, 类型: {transaction[1]}, 金额: ¥{transaction[2]}")  # Show transaction details

    def main_menu(self):
        # Main menu function for the ATM system
        while True:
            print("\n欢迎使用ATM系统")
            print("1. 查询余额")
            print("2. 存款")
            print("3. 取款")
            print("4. 查看交易记录")
            print("5. 退出系统")
            choice = input("请选择操作（1-5）：")  # Prompt user to choose operation

            if choice == '1':
                self.check_balance()  # Call balance checking function
            elif choice == '2':
                try:
                    amount = float(input("请输入存款金额："))  # Prompt for deposit amount
                    self.deposit(amount)  # Call deposit function
                except ValueError:
                    print("请输入有效的金额")  # Display error if invalid input
            elif choice == '3':
                try:
                    amount = float(input("请输入取款金额："))  # Prompt for withdrawal amount
                    self.withdraw(amount)  # Call withdrawal function
                except ValueError:
                    print("请输入有效的金额")  # Display error if invalid input
            elif choice == '4':
                self.show_history()  # Call transaction history function
            elif choice == '5':
                print("感谢使用ATM系统，再见！")  # Exit message
                sys.exit()  # Exit the program
            else:
                print("无效选项，请重新选择")  # Display error if invalid option

# Instantiate and run the ATM
atm = ATM()  # Create an instance of the ATM class
atm.main_menu()  # Start the main menu
