'''
This file is not an actual blockchain. It's hardcoded Python that I used to prepare the design of the actual app which could be found in /py-blockchain/app.py

You can run this in your terminal to play around with it as well. x
'''

# create users class
class Users:
    def __init__(self, address, key, id, wallet_id):
        self.address = address
        self.key = key
        self.id = id
        self.wallet_id = wallet_id


    def transactor(self):
        print("Your transaction is in progress...")


# create user object : 
user1 = Users("a1", "k1", "i1", "w1")


# test out transactions
print("Hello, enter the address for the person you will be sending a transaction to ")
info = input("Address: ")

if(info != user1.address):
    print("Sorry, a user with that address cannot be found. Please enter a new address to try again : ")

info = input("Address: ")

amount = input("Amount: ")
print("You will be sending " + amount + " to user " + info + ". Is this correct? ")
confirm = input(" Y / N : ")

if(confirm == "Yes" or confirm == "yes"):
    user1.transactor()
    print("You have successfully sent " + amount + " to " + info)

# async def confirmation():
#     if(confirm == "Yes" or confirm == "yes"):
#         await user1.transactor()
#         await asyncio.sleep(5) 
#         print("You have successfully sent " + amount + " to " + info)

# confirmation()

