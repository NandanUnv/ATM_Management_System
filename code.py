
import time

print("Welcome to ATM")

us_nm = ['Abhi', 'Balu', 'Chandini', 'Danush']
pass_w = ['8073', '35535', '2727', '9066']
balance = [1000, 5000, 2500, 6000]

cred = dict(zip(us_nm, pass_w))
enq = dict(zip(us_nm, balance))

u = input("Enter user_name:")
p = input("Enter password:")

def ferari(u):
    print('''Choose any one:\n1. Savings\n2. Current''')
    sc = input("Enter select your option(1/2):")
    if sc == '1':
        print('''1. Check Balance\n2. Withdraw''')
        scop = input("Enter select your option(1/2):")
        if scop == '1':
            print(f"Your balance:{enq[u]}")
        else:
            w_d = int(input("Enter your amount:"))
            if (w_d > enq[u]):
                print("Insufficient Balance")
            else:
                print("Please take the cash")
                time.sleep(3)
                enq[u] = enq[u] - w_d
                print(f"Your Balance: {enq[u]}")
    else:
        print('''1. Check Balance\n2. Withdraw''')
        scop = input("Enter select your option(1/2):")
        if scop == '1':
            print(f"Your balance:{enq[u]}")
        else:
            w_d = int(input("Enter your amount:"))
            if (w_d > enq[u]):
                print("Insufficient Balance")
            else:
                print("Please take the cash")
                enq[u] = enq[u] - w_d
                print(f"Your Balance: {enq[u]}")

if u in us_nm:
    if p == cred[u]:
        ferari(u)
        print("Thank you! visit again")
    else:
        print("Invalid Username or Password")
        pg = input("Do you want to Try again?(Y/N):")
        if pg=='Y' or pg =='y':
            p = input("Re-enter password:")
            if p == cred[u]:
                ferari(u)
                print("Thank you! visit again")
        else:
            print("Thank you! visit again")
            
