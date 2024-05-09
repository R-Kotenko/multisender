import time
import requests
import hmac
from hashlib import sha256
from config import *


def withdraw_from_bingX(to_address, amount, coin, network):
    payload = {}
    path = '/openApi/wallets/v1/capital/withdraw/apply'
    method = "POST"
    paramsMap = {
    "address": to_address,
    "addressTag": "None",
    "amount": amount,
    "coin": coin,
    "network": network,
    "timestamp": int(time.time() * 1000),
    "walletType": "1"
}
    paramsStr = praseParam(paramsMap)
    return send_request(method, path, paramsStr, payload)


def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    return signature


def send_request(method, path, urlpa, payload):
    url = "%s%s?%s&signature=%s" % (api_url_bing, path, urlpa, get_sign(api_secret_key_bing, urlpa))
    headers = {
        'X-BX-APIKEY': api_public_key_bing,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text


def praseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsStr = "&".join(["%s=%s" % (x, paramsMap[x]) for x in sortedKeys])
    return paramsStr+"&timestamp="+str(int(time.time() * 1000))


