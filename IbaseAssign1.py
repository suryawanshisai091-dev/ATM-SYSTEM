import csv

file = "bank.csv"

# Create CSV file with headers if it doesn't exist
try:
    f = open(file, mode="r")
    f.close()
except FileNotFoundError:
    with open(file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Mobile", "Balance"])


def add_new():
    name = input("Enter Your Name: ")
    mobile = input("Enter Mobile Number: ")
    balance = float(input("Enter Opening Balance: "))

    with open(file, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, mobile, balance])

    print("Account Created Successfully!")


def deposit_money():
    mobile = input("Enter Mobile Number: ")
    amount = float(input("Enter Amount to Deposit: "))

    rows = []
    found = False

    with open(file, mode="r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    for row in rows[1:]:
        if row[1] == mobile:
            row[2] = str(float(row[2]) + amount)
            found = True
            break

    if found:
        with open(file, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print("Money Deposited Successfully!")
    else:
        print("Account Not Found!")


def withdrawal_money():
    mobile = input("Enter Mobile Number: ")
    amount = float(input("Enter Amount to Withdraw: "))

    if amount <= 0:
        print("Enter a Valid Amount!")
        return

    rows = []
    found = False

    with open(file, mode="r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    for row in rows[1:]:
        if row[1] == mobile:
            balance = float(row[2])
            if amount <= balance:
                row[2] = str(balance - amount)
                found = True
            else:
                print("Insufficient Balance!")
                return
            break

    if found:
        with open(file, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print("Money Withdrawn Successfully!")
    else:
        print("Account Not Found!")


def view_balance():
    mobile = input("Enter Mobile Number: ")

    with open(file, mode="r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            if row[1] == mobile:
                print("Name:", row[0])
                print("Current Balance: Rs.", row[2])
                return

    print("Account Not Found!")


def menu():
    while True:
        print("\nWELCOME TO THE BANK..!")
        print("1. Add New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_new()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdrawal_money()
        elif choice == "4":
            view_balance()
        elif choice == "5":
            print("Thank You!")
            print("Rate My Code...!")
            break
        else:
            print("Invalid Choice!")


menu()
