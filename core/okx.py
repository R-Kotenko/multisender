import okx.Funding as Funding
from core.utils.untils import *
from config import *


def initialize_api(apikey, secretkey, passphrase, flag="0"):
    return Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)


fundingAPI = initialize_api(api_public_key_okx, api_secret_key_okx, pass_pharase_okx)


# def handle_make_withdrawal(response, to_address, amount, currency):
#     if response.get('code') == '0':
#         log.success(f"{to_address} | {amount} {currency} | successfully withdrawal")
#         return True
#     else:
#         log.warning(f"{to_address} | {amount} {currency} | {response.get('msg')} | error code: {response.get('code')}")
#         return False


def withdrawal_from_okx(to_address, amount, currency, chain):
    api = fundingAPI
    result = api.withdrawal(ccy=currency,
                            toAddr=to_address,
                            amt=amount,
                            fee=okx_fee,
                            dest=destination,
                            chain=chain)
    return result
