import json

from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS

import blockchain
from block import Block
from node import Node
from transaction import Transaction
from wallet import initialize_wallet, import_wallet_from_file

if __name__ == "__main__":
    from datetime import datetime

    transactions = []
    transaction_data = {'from': 'Darko', 'to': 'Igor', 'value': '30', 'timestamp': '2011-11-04 00:05:23.111'}
    transactions.append(transaction_data)
    transaction_data = {'from': 'Igor', 'to': 'Stefan', 'value': '10', 'timestamp': '2012-11-07 00:05:13.222'}
    transactions.append(transaction_data)
    transaction_data = {'from': 'Stefan', 'to': 'Darko', 'value': '10', 'timestamp': '2013-11-09 00:11:13.333'}
    transactions.append(transaction_data)
    transaction_data = {'from': 'Darko', 'to': 'Stefan', 'value': '20', 'timestamp': '2014-11-04 00:05:23.111'}
    transactions.append(transaction_data)
    transaction_data = {'from': 'Stefan', 'to': 'Igor', 'value': '5', 'timestamp': '2015-11-07 00:05:13.222'}
    transactions.append(transaction_data)
    transaction_data = {'from': 'Stefan', 'to': 'Darko', 'value': '10', 'timestamp': '2016-11-09 00:11:13.333'}
    transactions.append(transaction_data)

    timestamp_0 = datetime.timestamp(datetime.fromisoformat('2011-11-04 00:05:23.111'))

    block_0 = Block(
        transactions=transactions,
        timestamp=timestamp_0
    )

    timestamp_1 = datetime.timestamp(datetime.fromisoformat('2011-11-07 00:05:13.222'))
    block_1 = Block(
        transactions=transactions,
        timestamp=timestamp_1,
        previous_block=block_0
    )

    timestamp_2 = datetime.timestamp(datetime.fromisoformat('2011-11-09 00:11:13.333'))
    block_2 = Block(
        transactions=transactions,
        timestamp=timestamp_2,
        previous_block=block_1
    )

    b = blockchain.Blockchain()
    b.append_block(block_0)
    b.append_block(block_1)
    b.append_block(block_2)

    # print('--------------------------------------------------------------')
    # print(block_0)
    # print(block_1)
    # print(block_2)
    # print('--------------------------------------------------------------')

    # b.proof_of_work()

    f1 = open('./wallets/wallet_A_private.der', 'rb')
    f2 = open('./wallets/wallet_B_private.der', 'rb')
    f3 = open('./wallets/wallet_C_private.der', 'rb')
    f4 = open('./wallets/wallet_D_private.der', 'rb')
    f5 = open('./wallets/wallet_E_private.der', 'rb')
    f6 = open('./wallets/wallet_F_private.der', 'rb')

    wallet_A = import_wallet_from_file(ECC.import_key(f1.read()))
    wallet_B = import_wallet_from_file(ECC.import_key(f2.read()))
    wallet_C = import_wallet_from_file(ECC.import_key(f3.read()))
    wallet_D = import_wallet_from_file(ECC.import_key(f4.read()))
    wallet_E = import_wallet_from_file(ECC.import_key(f5.read()))
    wallet_F = import_wallet_from_file(ECC.import_key(f6.read()))

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()

    transaction = Transaction(wallet_A, wallet_B.public_key, 20)
    transaction.sign()

    node = Node(block_2)
    node.proof_of_work_test()

    # # print("POTPIS TEST 1: " + transaction.signature)
    # print("PODACI TEST 1: " + str(bytearray(json.dumps(transaction.generate_transaction_data(), indent=4).encode('utf-8'))))
    # boolean = node.verify_signature(wallet1.public_key, transaction.signature,  bytearray(json.dumps(transaction.generate_transaction_data(), indent=4).encode('utf-8')))
    # #
    # print(boolean)
    # print("\n\n ajmo")
    #
    # key = ECC.generate(curve='P-256')
    # h = SHA256.new(b"123")
    # signer = DSS.new(key, 'fips-186-3')
    # signature = signer.sign(h)
    # verifier = DSS.new(key.public_key(), 'fips-186-3')
    # verifier.verify(h, signature)
    # print(key)
    # print(key.public_key())

