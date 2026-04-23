class BankAccount:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.__pin = pin
        self.__balance = balance

    # Verify PIN
    def verify_pin(self, pin):
        return self.__pin == pin

    # Deposit money
    def deposit(self, amount, pin):
        if not self.verify_pin(pin):
            print("❌ Wrong PIN")
            return

        if amount > 0:
            self.__balance += amount
            print("✅ Amount Deposited:", amount)
        else:
            print("❌ Invalid Amount")

    # Withdraw money
    def withdraw(self, amount, pin):
        if not self.verify_pin(pin):
            print("❌ Wrong PIN")
            return

        if amount <= self.__balance:
            self.__balance -= amount
            print("✅ Withdrawn:", amount)
        else:
            print("❌ Insufficient Balance")

    # Get balance
    def get_balance(self, pin):
        if not self.verify_pin(pin):
            print("❌ Wrong PIN")
            return
        return self.__balance


# Child class (ATM Machine)
class ATM(BankAccount):

    def access_balance(self, pin):
        if not self.verify_pin(pin):
            print("❌ Wrong PIN")
            return
        print("💰 Balance (ATM Access):", self._BankAccount__balance)

    def change_pin(self, old_pin, new_pin):
        if self._BankAccount__pin == old_pin:
            self._BankAccount__pin = new_pin
            print("✅ PIN Changed Successfully")
        else:
            print("❌ Wrong Old PIN")


# ----------- Main Program -----------
user = ATM("SHYAM PRAJAPAT", 1234, 1000)

while True:
    print("\n====== 🏧 ATM MENU ======")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. ATM Internal Balance")
    print("5. Change PIN")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pin = int(input("Enter PIN: "))
        amt = int(input("Enter amount to deposit: "))
        user.deposit(amt, pin)

    elif choice == 2:
        pin = int(input("Enter PIN: "))
        amt = int(input("Enter amount to withdraw: "))
        user.withdraw(amt, pin)

    elif choice == 3:
        pin = int(input("Enter PIN: "))
        bal = user.get_balance(pin)
        if bal is not None:
            print("💰 Balance:", bal)

    elif choice == 4:
        pin = int(input("Enter PIN: "))
        user.access_balance(pin)

    elif choice == 5:
        old = int(input("Enter old PIN: "))
        new = int(input("Enter new PIN: "))
        user.change_pin(old, new)

    elif choice == 6:
        print("👋 Thank you for using ATM")
        break

    else:
        print("❌ Invalid Choice")