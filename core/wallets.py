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



# def seed():
#     if exists(path='mnemonic_dop.txt'):
#         with open(file='mnemonic_dop.txt', mode='r', encoding='utf-8-sig') as file:
#             seed_list = [row.strip() for row in file]
#     else:
#         seed_list = []
#
#     log.info(f"Downloaded successfully cookies: {len(seed_list)} in Base64")
#
#     try:
#         for seed in seed_list:
#
#             # split_list = dop_data[1:-1].split(', ')
#             #
#             # # Видаляємо одинарні лапки з кожного елемента
#             # new_list = [element.strip("'") for element in split_list]
#
#             # print(type(new_list))
#             # print(dop_data)
#
#             # data = ' '.join(new_list)
#             # print(data)
#
#             key = get_private_key(seed)
#
#
#             address = get_address(key)
#
#
#             with open('data_dop.txt', 'a') as file:
#                 file.write(f"{address}:{key}:{seed}\n")
#
#         log.success('Converter successfully in JSON')
#
#     except Exception as err:
#         log.error(err)


