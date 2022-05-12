
# Create a Blockchain using python

Blockchain is a shared, immutable digital technique that stores transactions over a decentralized network of computers.


## Screenshots
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Blockchain-using-Python/main/Screenshots/how-blockchain-work.png)

![App Screenshot](https://raw.githubusercontent.com/shaurya121/Blockchain-using-Python/main/Screenshots/blockchain_screenshot.png)



## Usage/Examples

Module to generate encrypted messges:
```python
import hashlib
```

Create object of class Blockchain:
```python
myblockchain=Blockchain()
```

Store transactions in the form of strings:
```python
t1='Vansh sends Rs. 5 to Shaurya'
t2='Shaurya sends Rs. 20  to Tushar'
t3='Tushar sends Rs. 40 to Rohit'
t4='Rohit sends Rs. 11 to Ritik'
```

Now create a Blockchain:
```python
myblockchain.create_block_from_transactions([t1, t2])
myblockchain.create_block_from_transactions([t3,t4])
```

Print the Blockchain:
```python
myblockchain.display_chain()
```
