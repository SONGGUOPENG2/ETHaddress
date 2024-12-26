from multiprocessing import Process
import os

import mnemonic
import bip32
import bip39
import re
from mnemonic import Mnemonic
from web3 import Web3
import web3
import eth_account
"""
2024.12.18
songuop@gmail.com 版权所有
copyright@SONGGUOPENG all rights have been reserved
"""

# 将地址写入桌面txt文件
def write_address_to_file(address,words):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop, "output.txt")
    with open(file_path, 'a') as file:
        file.write(address +'\n'+ words +'\n')

# 主要的处理逻辑
def songguopeng():
    print("开始计算！")
    i=0
    while True:
        mnemonic_words = mnemonic.Mnemonic(language='english').generate(strength=128)
        seed = bip39.phrase_to_seed(phrase=mnemonic_words)
        prvkey = bip32.BIP32.from_seed(seed).get_privkey_from_path("m/44'/60'/0'/0/0")
        address = eth_account.Account.from_key(prvkey).address

        if address[2:10].isdigit() and address[-7:].isdigit():
            words = mnemonic_words.split()
            wordspai = ' '.join(words)
            if "00000" in address[2:6]:
                wordspai = "零开头数字：\n" + wordspai
            elif re.search(r'(\d)\1{4,}', address):
                wordspai = "相同数字：\n" + wordspai
            elif address.count('0') > 10:
                wordspai = "大量相同零数字：\n" + wordspai
            elif address[-40:].isdigit():
                wordspai="惊现全数字：\n"+wordspai

            write_address_to_file(address, wordspai)
            print("**************地址已写入桌面txt文件****************")

"""
1.每秒100，太慢
mnemonic_words = mnemonic.Mnemonic(language='english').generate(strength=128)
eth_address=eth_account.Account.enable_unaudited_hdwallet_features()
eth_address = eth_account.Account.from_mnemonic(mnemonic_words).address

2.每秒300
seed = bip39.phrase_to_seed(phrase=mnemonic_words)
pubkey=bip32.BIP32.from_seed(seed).get_pubkey_from_path("m/44'/60'/0'/0/0")
prvkey=bip32.BIP32.from_seed(seed).get_privkey_from_path("m/44'/60'/0'/0/0")
address=eth_account.Account.from_key(prvkey).address
"""