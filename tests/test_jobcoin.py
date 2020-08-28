#!/usr/bin/env python
import pytest

import os
import sys
sys.path.append(os.path.realpath('.'))

from ..jobcoin import jobcoinnode

base_url  = 'http://jobcoin.gemini.com/tinderbox-unmapped/api'

@pytest.fixture
def response():
    import requests
    return requests.get('https://jobcoin.gemini.com/')


def test_get_balance():
  import requests
  jobCoinAPI = JobCoinAPI(base_url)
  address = "Alice"
  response = JobCoinAPI.get_balance(address)
  return response

def test_address_generator():
  print("Address Generator Test")
  print(address_generator(32))


"""
TESTING JOBCOIN API WRAPPER
"""

def test_get_balance():
  address = "Alice"
  response = get_balance(address)
  return response

def test_post_transactions():
  source_address = "Alice"
  destination_address = "Bob"
  amount = 7.2
  resp = post_transactions(source_address, destination_address, amount)
  print(resp.json())
  return

def test_get_transactions():
  return get_transactions().json()

def test_does_address_exist():
  address = "Alice"
  print(does_address_exist(address))

  address = "asdkfansdui3i8"
  print(does_address_exist(address))

