import subprocess
import time
import re
import datetime
import sys
from commons import Commons
from decimal import Decimal

commons = Commons()

today = datetime.datetime.now().strftime("%Y-%m-%d")
today = '2018-10-01'

# user,producer_num,balance
output_results_file = './data/airdrop_results_%s.txt' % today

total = Decimal(0)

with open(output_results_file, 'r') as f:
	for line in f:
		line = line.rstrip()
		tokens = commons.safe_split_limit(line, ',', 2)
		balance = tokens[1]
		total = total + Decimal(balance)
		print('%s' % total)
