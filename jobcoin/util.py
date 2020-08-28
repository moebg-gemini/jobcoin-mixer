# -*- coding: utf-8 -*-
import random
import string

def address_generator(length=16):
  if length < 0 or length > 32:
    return -1

  output = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
  return output

