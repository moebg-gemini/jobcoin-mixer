#!/usr/bin/env python
import sys
import json

import click

from jobcoin.config import ClientConfig
from jobcoin.client import Client
from jobcoin.mixer import Mixer


@click.command()
def main(args=None):
    print('Welcome to the Jobcoin mixer!\n')

    # Load config
    with open('./config.json') as conf:
      config_dict = json.load(conf)

    # Create User client
    client_config = ClientConfig(config_dict)
    client = Client(client_config)

    while True:
        # User inputs a list of new address for mixed coins to be sent
        addresses_num = click.prompt(
            'Please enter the number of output addresses you want for mixing ',
            prompt_suffix='\n[blank to quit] > ',
            default='',
            show_default=False)
        if addresses_num.strip() == '':
            sys.exit(0)

        addresses_num = float(addresses_num)
        amount = click.prompt(
            'Please enter the amount of coins to transfer ',
            prompt_suffix='\n[blank to quit] > ',
            default='',
            show_default=False)

        amount = float(amount)
        client.create_new_output_addresses()

        # Create a new deposit address for the mixer
        mixer = Mixer()
        
        print("Creating mixer job")
        deposit_address = mixer.create_mixer_job(client.output_addresses, amount)
        user_address = "default_user_wallet"

        print("Transferring funds from user address to deposit address")
        resp = client.transfer_funds_to_deposit(user_address, deposit_address, amount)

        print("Checking deposit address for valid transfer")
        check = mixer.poll_users_deposit_account(deposit_address)

        print("Transfering coins from deposit to pool and executing mix")        
        mixer.transfer_deposit_to_pool(deposit_address)
        mixer.mix_coins(deposit_address)
        print("-------------------------------")


if __name__ == '__main__':
    sys.exit(main())
