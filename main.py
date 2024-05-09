import random
from config import *
from core.wallets import *
from core.bybit import withdraw_from_bybit
from core.bingx import withdraw_from_bingX
from core.okx import withdrawal_from_okx
import json


def main():
    if exists(path='data/address.txt'):
        with open(file='data/address.txt', mode='r', encoding='utf-8-sig') as file:
            address_list = [row.strip() for row in file]
    else:
        address_list = []

    if exists(path='data/keys.txt'):
        with open(file='data/keys.txt', mode='r', encoding='utf-8-sig') as file:
            keys_list = [row.strip() for row in file]
    else:
        keys_list = []

    if exists(path='data/mnemonic.txt'):
            with open(file='data/mnemonic.txt', mode='r', encoding='utf-8-sig') as file:
                mnemonic_list = [row.strip() for row in file]
    else:
        mnemonic_list = []

    if exists(path='data/new_wallets.txt'):
        with open(file='data/new_wallets.txt', mode='r', encoding='utf-8-sig') as file:
            new_wallets_list = [row.strip() for row in file]
    else:
        new_wallets_list = []

    log.success(f"Downloaded successfully address: {len(address_list)} | keys: {len(keys_list)}")
    log.success(f"Downloaded successfully mnemonic: {len(mnemonic_list)} | new wallets: {len(new_wallets_list)}")

    time.sleep(1)

    software_method = int(input('\n1.Create EVM wallets\n'
                                '2. Get private key from seed phrase\n'
                                '3. Get address from private key\n'
                                '4. Multisender from OKX\n'
                                '5. Multisender from Bing-X\n'
                                '6. Multisender from ByBit\n'
                                'Make your choice:\n'))
    print()

    if software_method == 1:
        counter = 0
        log.debug('How many wallets you want to generate:\n')
        counter_wallets = int(input())
        for i in range(counter_wallets):
            counter += 1
            log.info(f"Work progress: {counter}/{counter_wallets} | in line: {counter_wallets - (counter)}")
            wallets_creator()

    elif software_method == 2:
        counter = 0
        for mnemonic in mnemonic_list:
            counter += 1
            log.info(
                f"Work progress: {counter}/{len(mnemonic_list)} | in line: {len(mnemonic_list) - counter}")
            private_key = get_private_key(mnemonic)
            with open('data/private_key_from_mnemonic.txt', 'a') as file:
                file.write(f'{private_key}\n')

    elif software_method == 3:
        counter = 0
        for key in keys_list:
            counter += 1
            log.info(
                f"Work progress: {counter}/{len(keys_list)} | in line: {len(keys_list) - counter}")
            if len(key) == 66:
                address = get_address(key)
                with open('data/address_from_key.txt', 'a') as file:
                    file.write(f'{address}\n')
            elif len(key) == 0:
                continue
            else:
                log.warning(f"{key} | is not private key")

    elif software_method == 4:
        counter = 0
        for to_address in address_list:
            counter += 1
            log.info(
                f"Sending progress: {counter}/{len(address_list)} | in line: {len(address_list) - counter}")

            amount = round(random.uniform(amount_between[0], amount_between[1]), 6)
            withdraw = withdrawal_from_okx(to_address, amount, currency, chain)

            if int(withdraw["code"]) == 0:
                log.success(f'{to_address} | send successfully | {amount}{currency}')

            else:
                log.warning(f"{to_address} | {withdraw}")
                with open('data/address_failed_sending.txt', 'a') as file:
                    file.write(f'{to_address}\n')

            tm = random.randint(random_pause[0], random_pause[1])
            sleeping(tm)
        print()

    elif software_method == 5:
        counter = 0
        for to_address in address_list:
            counter += 1
            log.info(
                f"Sending progress: {counter}/{len(address_list)} | in line: {len(address_list) - counter}")

            amount = round(random.uniform(amount_between[0], amount_between[1]), 6)
            withdraw = json.loads(withdraw_from_bingX(to_address, amount, currency, chain))

            if withdraw["code"] == 0:
                log.success(f'{to_address} | send successfully | {amount}{currency}')

            else:
                log.warning(f"{to_address} | {withdraw}")
                with open('data/address_failed_sending.txt', 'a') as file:
                    file.write(f'{to_address}\n')

            tm = random.randint(random_pause[0], random_pause[1])
            sleeping(tm)
        print()

    elif software_method == 6:
        counter = 0
        for to_address in address_list:
            counter += 1
            log.info(
                f"Sending progress: {counter}/{len(address_list)} | in line: {len(address_list) - counter}")

            amount = round(random.uniform(amount_between[0], amount_between[1]), 6)
            withdraw = withdraw_from_bybit(to_address, amount)

            if withdraw:
                log.success(f'{to_address} | send successfully | {amount}{currency}')

            else:
                with open('data/address_failed_sending.txt', 'a') as file:
                    file.write(f'{to_address}\n')

            tm = random.randint(random_pause[0], random_pause[1])
            sleeping(tm)
        print()

    else:
        log.warning("Unknown method, choose 1,2,3,4,5 or 6!")

    print()
    log.debug('The work is completed..')


if __name__ == '__main__':
    main()
