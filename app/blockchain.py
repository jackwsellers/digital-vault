import requests
import socket
import json
import re

def get_from_bitcoind(method, params=[]):
    """response = get_from_bitcoind('getreceivedbyaddress',
                                    'msT1xh5vQ6ZsT3XhdNXFJ4XvEzmvwVfNMS')"""
    url = 'http://admin:adminpw@ec2-13-228-250-145.ap-southeast-1.compute.amazonaws.com:18332/wallet/DigitalVault'
    headers = {'content-type': 'application/json'}
    payload = {
        'method': method,
        'params': params,
        'jsonrpc': '2.0',
        'id': 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    if response['error'] is None:
        return response['result']
    else:
        return response['error']


def get_from_electrum(method, params=[]):
    """response = get_from_electrum('blockchain.address.get_balance',
                                    'msT1xh5vQ6ZsT3XhdNXFJ4XvEzmvwVfNMS')"""
    params = [params] if type(params) is not list else params
    s = socket.create_connection(('206.189.29.167', 50001))
    s.send(json.dumps({'id': 0, 'method': method,
                       'params': params}).encode() + b'\n')
    response = json.loads(s.recv(99999)[:-1].decode())
    return response

# def search_blockchain(search):
#     try:
#         # address ???
#         data = get_from_bitcoind('getblock', [search])
#         data['message']
#         try:            
#             height_to_hash = get_from_bitcoind('getblockhash', [search])
#             data = get_from_bitcoind('getblock', [height_to_hash])
#             data['message']
#             try:
#                 data = get_from_bitcoind('getrawtransaction', [search, 1])
#                 data['message']
#                 category = None
#                 search_id = None
#             except KeyError:
#                 category = 'tx'
#                 search_id = search
#         except KeyError:
#             category = 'block'
#             search_id = search
#     except KeyError:
#         category = 'block'
#         search_id = data['height']
#     print('category: ', category)
#     print('search_id: ', search_id)
#     #print('data: ', data)
#     return category, search_id, data

def search_blockchain_block(search):
    data = get_from_bitcoind('getblock', [search])
    return data

def search_blockchain_height(search):
    if search == "" or not re.match("^[0-9]*$", search): 
        searchID = str(search)
    else: 
        searchID = int(search)
    
    height_to_hash = get_from_bitcoind('getblockhash', [searchID])
    data = get_from_bitcoind('getblock', [height_to_hash])
    return data

def search_blockchain_tx(search):
    data = get_from_bitcoind('getrawtransaction', [search, 1])
    return data

def search_blockchain_address(search):
    address_info = []
    data = get_from_bitcoind('listreceivedbyaddress', [0, bool(1), bool(1)])
    for item in data:
        #print("items.......",item['address'])
        if item['address'] == search:
            address_info.append(item)
            #print("addsedd...........",address_info)
    return address_info

def get_raw_mempool():
    tx_ids = []
    raw_mempool = get_from_bitcoind('getrawmempool')
    for tx_id in raw_mempool:
        tx_ids.append({'tx_id': tx_id})
    return tx_ids
