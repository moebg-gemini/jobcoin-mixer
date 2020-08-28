# -*- coding: utf-8 -*-
from jobcoin.jobcoinapi import *
from jobcoin.util import address_generator

class Client:
  def __init__(self, client_config, output_addresses=[]):
    self.output_addresses = output_addresses
    self.api_base_url = client_config.api_base_url
    self.api_address_url = client_config.api_address_url
    self.api_transactions_url = client_config.api_transactions_url
    self.default_addr_min = client_config.default_addr_min
    self.default_addr_length = client_config.default_addr_length

  def create_new_output_addresses(self, addr_input=None):
    output_addresses = []
    total_addr = addr_input
    if addr_input == None:
      total_addr = self.default_addr_min

    for i in range(0, total_addr):
      addr = address_generator(self.default_addr_length)
      if does_address_exist(addr) == False:
        output_addresses.append(addr)
    self.output_addresses = output_addresses
    return output_addresses

  def transfer_funds_to_deposit(self, source_address, deposit_address, amount):
    resp = post_transactions(source_address, deposit_address, amount)
    return resp
