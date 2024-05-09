from pybit.unified_trading import HTTP
from core.utils.untils import *
from config import *
from time import time
from pybit import _v5_asset


# def get_coin_info(coin_symbol):
#     session = HTTP(
#         testnet=False,
#         api_key=api_public_key_bybit,
#         api_secret=api_secret_key_bybit,
#     )
#     print(session.get_coin_info(
#         coin=coin_symbol,
#     ))
#
# get_coin_info('ETH')


_session = _v5_asset.AssetHTTP(api_key=api_public_key_bybit, api_secret=api_secret_key_bybit)

def withdraw_from_bybit(to_address, amount):
    try:
        return _session.withdraw(
            coin=currency,
            chain=chain,
            address=to_address,
            amount=str(amount),
            timestamp=int(time() * 1000),
        )
    except Exception as err:
        log.warning(f"{to_address} | {err}")
        return False







