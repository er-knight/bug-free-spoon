# https://youtu.be/ZhnJ1bkIWWk

from hashlib import sha256

MAX_NONCE = 10000000

def SHA256(text):
	return sha256("ABC".encode("utf-8")).hexdigest()
	
def mine(block_number, transactions, previous_hash, prefix_zeroes=20):

	prefix_str = "0" * prefix_zeroes

	for nonce in range(MAX_NONCE):
		text = f"{block_number}{transactions}{previous_hash}{nonce}"
		new_hash = SHA256(text)
		
		if new_hash.startswith(prefix_str):
			print(f"Yay! Successfully mined bitcoins with nonce value: {nonce}")
			return new_hash
			
	raise Exception(f"Couldn't find correct hash after trying {MAX_NONCE} time")
	
if __name__ == "__main__":

	transactions = "".join([
		"steve->tony->45",
		"harry->ron->31"
	])
	
	difficulty = 4 # number of zeroes in front of hash
	
	new_hash = mine(5, transactions, "0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7", difficulty)
	
	print(new_hash)
