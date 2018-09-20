#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import subprocess
import time
from pprint import pprint
import datetime

less_than_ten_producers = 0
less_than_twenty_producers = 0
less_than_thirty_producers = 0
more_than_thirty_producers = 0
total = 0

today = datetime.datetime.now().strftime('%Y-%m-%d')
#today = '2018-08-30'
with open('./data/voter_accounts_%s.txt' % today, 'r') as f:
    for line in f:
        if line.rstrip() == '':
            continue

        if ',' not in line.rstrip():
            continue

        line = line.rstrip()
        tokens = line.split(',')
        user = tokens[0]
        producers = int(tokens[1])

        if producers >= 0 and producers < 10:
            less_than_ten_producers = less_than_ten_producers + 1
            total = total + 1

        if producers >= 10 and producers < 20:
            less_than_twenty_producers = less_than_twenty_producers + 1
            total = total + 1

        if producers >= 20 and producers < 30:
            less_than_thirty_producers = less_than_thirty_producers + 1
            total = total + 1

        if producers >= 30:
            more_than_thirty_producers = more_than_thirty_producers + 1
            total = total + 1

    print('Voting for less than 10 producers: %s voters or %s%%' % (less_than_ten_producers, '{0:.2f}'.format(less_than_ten_producers / total * 100) ))
    print('Voting for less than 20 producers: %s voters or %s%%' % (less_than_twenty_producers, '{0:.2f}'.format(less_than_twenty_producers / total * 100) ))
    print('Voting for less than 30 producers: %s voters or %s%%' % (less_than_thirty_producers, '{0:.2f}'.format(less_than_thirty_producers / total * 100) ))
    print('Voting for more than 30 producers: %s voters or %s%%' % (more_than_thirty_producers, '{0:.2f}'.format(more_than_thirty_producers / total * 100) ))
