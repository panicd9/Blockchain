wallet_A = initialize_wallet()
wallet_B = initialize_wallet()
wallet_C = initialize_wallet()
wallet_D = initialize_wallet()
wallet_E = initialize_wallet()
wallet_F = initialize_wallet()

f1 = open('/wallets/wallet_A.der', 'wt')
f2 = open('/wallets/wallet_B.der', 'wt')
f3 = open('/wallets/wallet_B.der', 'wt')
f4 = open('/wallets/wallet_B.der', 'wt')
f5 = open('/wallets/wallet_B.der', 'wt')
f6 = open('/wallets/wallet_B.der', 'wt')

f1.write(wallet_A.private_key.export_key(format='DER'))
f2.write(wallet_B.private_key.export_key(format='DER'))
f3.write(wallet_C.private_key.export_key(format='DER'))
f4.write(wallet_D.private_key.export_key(format='DER'))
f5.write(wallet_E.private_key.export_key(format='DER'))
f6.write(wallet_F.private_key.export_key(format='DER'))