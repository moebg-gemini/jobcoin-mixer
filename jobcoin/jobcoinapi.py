# -*- coding: utf-8 -*-
import requests
import json
import os


api_base_url = "http://jobcoin.gemini.com/tinderbox-unmapped/api"

def get_balance(address):
  if not address:
    return "Error"
  elif isinstance(address, str) == False:
    return "Error"

  resp = requests.get('{}/addresses'.format(api_base_url) + "/" + address)
  resp = (resp.json())["balance"]
  print(resp)
  balance = float(resp)
  return balance

def post_transactions(source_address, destination_address, amount):
  # Data validation error check -> not null, string type for all include the amount
  if source_address == None or destination_address == None or amount == None:
    return "Error"

  # Check amount to make sure transfer involves amount > 0.0
  if amount <= 0.0:
    return "Error"

  # Construct payload for POST request to be sent in body
  payload = {
    "fromAddress": source_address,
    "toAddress": destination_address,
    "amount": str(amount)
  }

  return requests.post('{}/transactions'.format(api_base_url), data=payload)

def get_transactions():
  return requests.get('{}/transactions'.format(api_base_url))

def does_address_exist(address):
  resp = requests.get('{}/addresses'.format(api_base_url) + "/" + address)
  resp = resp.json()
  if len(resp["transactions"]) == 0 and resp["balance"] == "0":
    return False

  return True


def create_coins_for_account(address):
  if not address:
    return "Error"
  elif isinstance(address, str) == False:
    return "Error"

  payload = {
    "address": address
  }
  resp = requests.post('{}/create'.format(api_base_url[:len(api_base_url) - 4]), data=payload)
  return
