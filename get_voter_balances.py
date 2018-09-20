import subprocess
import time
import re
import datetime
import sys
from commons import Commons
from command_builder import CommandBuilder

commons = Commons()
command_builder = CommandBuilder()
today = datetime.datetime.now().strftime("%Y-%m-%d")
#today = '2018-08-30'
output_results_file = './data/voter_balances_%s.txt' % today
p = open(output_results_file, 'a')

balance_errors_file = './data/voter_balance_errors_%s.txt' % today
e = open(balance_errors_file, 'a')

accounts_file = './data/voter_accounts_%s.txt' % today
#accounts_file = './data/missing_users_2018-08-13.txt'

with open(accounts_file, 'r') as f:
	for line in f:
		line = line.rstrip()
		tokens = commons.safe_split(line, ',', 2)
		user = tokens[0]
		producers = tokens[1]
		if commons.is_blank(user):
			print("No user found when splitting: `%s`" % line, file=sys.stderr)

		cmd = command_builder.build_get_account(user)
		balance = commons.get_correct_account_response_from_cmd(cmd, 'total')
		if balance is None:
			cmd = command_builder.build_get_account(user)
			print("Problem with cmd: `%s`" % (' '.join(cmd)), file=sys.stderr)
			e.write('%s,%s\n' % (user, producers))
			e.flush()
			continue

		p.write('%s,%s,%s\n' % (user, producers, balance.rstrip().replace(' ','')))
		print('%s,%s,%s' % (user, producers, balance.rstrip().replace(' ','')))
		#time.sleep(.5)
p.close()
e.close()
