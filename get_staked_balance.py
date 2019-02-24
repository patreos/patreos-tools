import subprocess
import time
import re
import datetime
import sys
import json

from decimal import *
from commons import Commons
from command_builder import CommandBuilder

commons = Commons()
command_builder = CommandBuilder()
today = datetime.datetime.now().strftime("%Y-%m-%d")
#today = '2018-09-19'

input_accounts_file = './data/staker_accounts_%s.txt' % today

data = []

with open(input_accounts_file, 'r') as f:
	for line in f:
		line = line.rstrip()
		user = line

		if commons.is_blank(user):
			print("No user found when splitting: `%s`" % line, file=sys.stderr)
			continue

		cmd = [
			'/Users/okayplanet/dev/eos/eos/build/programs/cleos/cleos',
            '--url',
            'https://api.eosnewyork.io',
			'get',
			'table',
			'patreostoken',
			'%s' % user,
			'stakes'
		]

		staked = json.loads(commons.cmd_exec(cmd))
		print("%s,%s" % (user, staked["rows"][0]["balance"]))
		data.append(staked["rows"][0]["balance"])

total = Decimal(0.0000)
for d in data:
	total = total + Decimal(d.replace(' PATR', ''))
print("Total is %s" % total)
