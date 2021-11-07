from block import Block
from time  import time_ns
from json  import dumps, loads

class BlockChain:

    def __init__(self) -> None:

        self.difficulty = 1
        self.chain      = [Block(timestamp=time_ns())]

    def __str__(self) -> str:

        return dumps(self.to_json(), indent=4)

    def last_block(self) -> Block:

        return self.chain[-1]

    def add_block(self, block) -> None:

        block.pre_hash = self.last_block()._hash()
        block.hash     = block._hash()

        success = block.mine_block(self.difficulty)

        if success:
            self.chain.append(block)

    def validate_chain(self) -> bool:

        for i in range(len(self.chain)):

            cur_block = self.chain[i]
            pre_block = self.chain[i - 1]

            if (cur_block.hash != cur_block._hash() or 
                cur_block.pre_hash != pre_block._hash()):
                return False

        return True

    def to_json(self) -> dict:

        return {
            "difficulty" : self.difficulty,
            "blockchain" : [
                block.to_json() for block in self.chain
            ]
        }

    def from_json(self, logs: dict) -> None:

        self.difficulty = logs["difficulty"]
        self.chain      = [
            Block(
                timestamp=block["timestamp"],
                data=block["data"],
                pre_hash=block["pre-hash"],
                nonce=block["nonce"]
            ) for block in sorted(
                logs["blockchain"], key=lambda item: item["timestamp"]
            )
        ]

if __name__ == "__main__":

    blockchain = BlockChain()

    with open("logs.json") as logs: 
        blockchain.from_json(loads(logs.read()))

    # blockchain.add_block(Block())
    # blockchain.add_block(Block())
    # blockchain.add_block(Block())

    print(blockchain)