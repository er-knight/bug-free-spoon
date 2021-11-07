from hashlib import sha256
from time    import time_ns
from json    import dumps

class Block:

    def __init__(self, 
        timestamp: int=None, 
        data: dict=None, 
        pre_hash: int=None,
        nonce: int=None) -> None:

        self.timestamp = timestamp if timestamp else time_ns()
        self.data      = data if data else {}
        self.pre_hash  = pre_hash
        self.nonce     = nonce if nonce else 0
        self.hash      = self._hash()

    def _hash(self) -> str:

        __hash = sha256()

        __hash.update(str(self.timestamp).encode("utf-8"))
        __hash.update(str(self.data).encode("utf-8"))
        __hash.update(str(self.pre_hash).encode("utf-8"))
        __hash.update(str(self.nonce).encode("utf-8"))

        return __hash.hexdigest()

    def __str__(self) -> str:

        return dumps(self.to_json(), indent=4)

    def to_json(self) -> dict:

        return {
            "timestamp": self.timestamp,
            "data": self.data,
            "pre-hash": self.pre_hash,
            "nonce": self.nonce,
            "hash": self.hash
        }

    def mine_block(self, difficulty) -> bool:

        MAX_NONCE = 10000
        
        pre_mine_nonce = self.nonce
        pre_mine_hash  = self.hash

        successful = False

        while (self.nonce <= MAX_NONCE):
            if self.hash.startswith("0" * difficulty):
                successful = True
                break

            self.nonce += 1
            self.hash   = self._hash()

        if not successful:
            self.nonce = pre_mine_nonce
            self.hash  = pre_mine_hash
            return False

        return True
        
if __name__ == "__main__":

    block = Block()
    print(block)