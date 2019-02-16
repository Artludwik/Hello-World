#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=~`<,.>?/\:;{}[]'
yourLength = input ('How many characters should have your new password ? Make a choice by giving a number:')
length = int(yourLength)
howManyPasswords = input ('How many passwords do you want to generate ? Please make a choice by entering a number:')
passNumb = int(howManyPasswords)
for p in range(passNumb):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)