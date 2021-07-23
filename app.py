
import hashlib

# initilize a class for the blockchain
class CCbagelBlock:
    # class initializer
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        # constructing data strings
        self.block_data = " - ".join(transaction_list) + " - " + previous_block_hash

        # calculate hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Mike sends Anna 2 CC"
t2 = "Bob sends Anna 4 CC"
t3 = "Anna sends 4 CC to Oscar"
t4 = "Oscar sends 30 CC to Jake"

initial_block = CCbagelBlock("First block initialized", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = CCbagelBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

'''
To test this out, you can download this project and run it in your terminal. Try changing the amount of CC sent in t1, t2, t3, t4 and compare the block hashes. 
'''