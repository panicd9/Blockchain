import json
from typing import List

from cryptography import calculate_hash
from transaction import Transaction


class Block:
    def __init__(self, timestamp: float, transactions: List[Transaction], previous_block=None):
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_block = previous_block
        self.previous_block_hash = ""

        if self.previous_block:
            self.previous_block_hash = previous_block.hash
        self.hash = self.find_hash()

    # @property
    # def previous_block_hash(self) -> str:
    #     previous_block_hash = ""
    #     if self.previous_block:
    #         previous_block_hash = self.previous_block_hash
    #     return previous_block_hash

    # @property
    def find_hash(self) -> str:
        block_data = {
            "transactions": str(self.transactions),
            "timestamp": self.timestamp,
            "previous_block_cryptographic_hash": self.previous_block_hash
        }
        block_data_bytes = json.dumps(block_data, indent=4).encode('utf-8')
        # block_data_bytes = json.dumps(block_data).encode('utf-8')
        # print(block_data_bytes)
        return calculate_hash(block_data_bytes)

    def proof_of_work_block(self):
        nonce = 0
        data_to_hash = self.hash + str(nonce)
        hash_to_find = calculate_hash(data_to_hash.encode('utf-8'))
        while hash_to_find[0:4] != "0000":
            # print(hash_to_find[0:3])
            data_to_hash = self.hash + str(nonce)
            hash_to_find = calculate_hash(data_to_hash.encode('utf-8'))
            # print("Nonce:" + str(nonce))
            # print(hash_to_find)
            nonce = nonce + 1
        print("Nonce:" + str(nonce))
        print(hash_to_find)

    def __str__(self):
        to_string = "Timestamp: \n\t" + \
                    str(self.timestamp) + \
                    "\nHash: \n\t" + \
                    self.hash + \
                    "\nTransactions:\n" + \
                    json.dumps(self.transactions, indent=4) + \
                    "\n"
        return to_string
