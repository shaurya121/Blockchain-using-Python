import hashlib	

# creating the block class
class GeeekCoinBlock():
	def __init__(self, previous_block_hash, transaction_list):
		self.previous_block_hash=previous_block_hash		#reference to prevoius block
		self.transaction_list=transaction_list		#list of txns made in the current block
		
		self.block_data=f"{' - '.join(transaction_list)} \nPREVIOUS HASH ---- {previous_block_hash}"
		self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()	

class Blockchain():
	def __init__(self):
		self.chain=[]
		self.generate_genesis_block()
		
	def generate_genesis_block(self):
		self.chain.append(GeeekCoinBlock("0", ["Genesis Block"]))
		
	def create_block_from_transactions(self, transaction_list):
		previous_block_hash=self.last_block.block_hash
		self.chain.append(GeeekCoinBlock(previous_block_hash, transaction_list))
		
	def display_chain(self):
		for i in range(len(self.chain)):
			print(f"DATA {i+1}: {self.chain[i].block_data}")
			print(f"HASh {i+1}: {self.chain[i].block_hash}\n")
	@property
	def last_block(self):
		return self.chain[-1]

# transactions list	
t1='Vansh sends Rs. 5 to Shaurya'
t2='Shaurya sends Rs. 20  to Tushar'
t3='Tushar sends Rs. 40 to Rohit'
t4='Rohit sends Rs. 11 to Ritik'
t5='Ritik sends Rs. 200 to Dravid'
t6='Dravid sends Rs. 100 to Naman'

myblockchain=Blockchain()
myblockchain.create_block_from_transactions([t1, t2])
myblockchain.create_block_from_transactions([t3,t4])
myblockchain.create_block_from_transactions([t5,t6])
myblockchain.display_chain()


		
	
