# -*- coding: utf-8 -*-
class ClientConfig:
  def __init__(self, config_dict):
    self.api_base_url = config_dict["api_base_url"]
    self.api_address_url = '{}/addresses'.format(config_dict["api_base_url"])
    self.api_transactions_url = '{}/transactions'.format(config_dict["api_base_url"])
    self.default_addr_min = config_dict["client_addr_min"]
    self.default_addr_length = config_dict["client_default_addr_length"]
