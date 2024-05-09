from core.utils.untils import *
from web3 import Account
from eth_account.account import LocalAccount
from os.path import exists
from mnemonic import Mnemonic


def get_private_key(mnemonic):
    Account.enable_unaudited_hdwallet_features()
    account = Account.from_mnemonic(mnemonic)
    return account._private_key.hex()


def get_address(private_key):
    address = Account.from_key(private_key).address
    return address


def wallets_creator():

    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(strength=128)

    private_key = get_private_key(seed_phrase)
    address = get_address(private_key)

    with open('data/new_wallets.txt', 'a') as file:
        file.write(f'{address}:{private_key}:{seed_phrase}\n')
        log.success(f"{address} | created successfully")
