# -*- coding: utf-8 -*-
from jobcoin.jobcoinapi import *
from jobcoin.util import address_generator

class Mixer:
  def __init__(self, charge_fee=False, fee=0):
    # pool_address: the Mixer's home address that pools all coins
    self.pool_address = address_generator()
    
    # mixer_jobs: map that keeps track of mixing jobs between deposit addresses and (amount, output addresss)
    self.mixer_jobs = {}
    
    # charge_fee: specifies whether this mixer charges a fee or not (boolean)
    self.charge_fee = charge_fee
    
    # fee: flat rate fee charged by the mixer for a mix request
    self.fee = fee


  def get_pool_amount(self):
    balance = get_balance(self.pool_address)
    return balance

  def transfer_deposit_to_pool(self, deposit_address):
    resp = post_transactions(deposit_address, self.pool_address, self.mixer_jobs[deposit_address][0])
    return resp

  def poll_users_deposit_account(self, deposit_address):
    # Check the deposit address for a balance where it must meet X amount that the mixer job demands
    amount_to_match = self.mixer_jobs[deposit_address][0]

    # O(1) check in hash table to get deposit address and how much should be in there
    balance_in_deposit_state = get_balance(deposit_address)

    # If the deposit address is filled with amount of coins, then transfer(deposit, pool_address) from another function
    if balance_in_deposit_state >= amount_to_match:
      return True

    # Use a different function in Mixer that runs the core algo for randomly distributing X coins to the N addresses
    return False

  def create_mixer_job(self, output_addresses, amount):
    # Create a fresh deposit address
    new_deposit_address = address_generator()

    # Check if it exists, if not try again
    while does_address_exist(new_deposit_address) == True:
      new_deposit_address = address_generator()

    # Insert the Mixer Job in hash table or a time queue
    self.mixer_jobs[new_deposit_address] = (amount, output_addresses)

    # Return the User the deposit address
    return new_deposit_address

  def mix_coins(self, deposit_address):
    # Grab N addresses
    output_addresses = self.mixer_jobs[deposit_address][1]
    N = len(output_addresses)

    # Get Amount
    amount = self.mixer_jobs[deposit_address][0]

    # Charge fee if the mixer charges a fee
    if self.charge_fee:
      amount -= fee

    transfer_amount = amount / N
    for i in range(0, len(output_addresses)):
      if amount < transfer_amount:
        transfer_amount = amount
      r = post_transactions(self.pool_address, output_addresses[i], transfer_amount)
      amount -= transfer_amount

    return
