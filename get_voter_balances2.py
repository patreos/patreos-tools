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
today = '2018-10-01'

# time,account,balance
input_snapshot_file = './data/%s_account_snapshot.csv' % today

# user,producer_num,balance
output_results_file = './data/voter_balances_%s.txt' % today
p = open(output_results_file, 'a')

# user,producer_num
output_balance_errors_file = './data/voter_balance_errors_%s.txt' % today
e = open(output_balance_errors_file, 'a')

# account,staked,producers
input_accounts_file = './data/voters%s.csv' % today
#input_accounts_file = './data/missing_users_2018-08-13.txt'

with open(input_accounts_file, 'r') as f:
	for line in f:
		line = line.rstrip()
		tokens = commons.safe_split_limit(line, ',', 3)
		user = tokens[0].replace('"', '')
		if user == "voter_name":
			continue;

		producer_string = tokens[2].replace('"', '')
		if commons.is_blank(producer_string):
			#print("User: %s is not a voter" % user)
			continue

		producers = len(producer_string.split(','))
		if producers <= 0:
			#print("User: %s is not a voter" % user)
			continue

		#print("string: %s and count: %s" % (producer_string, producers))
		if commons.is_blank(user):
			print("No user found when splitting: `%s`" % line, file=sys.stderr)
			continue

		cmd = command_builder.grep(",%s," % user, input_snapshot_file)
		snapshot_line = commons.cmd_exec(cmd) #time,account,balance
		if commons.is_blank(snapshot_line):
			print("Problem with cmd: `%s`" % (' '.join(cmd)), file=sys.stderr)
			e.write('%s,%s\n' % (user, producers))
			e.flush()
			continue

		snapshot_line_tokens = commons.safe_split(snapshot_line, ',', 3)
		if snapshot_line_tokens[1] != user:
			print("grep'd for user: %s but found: %s" % (user, snapshot_line_tokens[1]))
			e.write('%s,%s\n' % (user, producers))
			e.flush()
			continue
			#raise ValueError("grep'd for user: %s but found: %s" % (user, snapshot_line_tokens[1]))

		balance = snapshot_line_tokens[2]
		p.write('%s,%s,%s\n' % (user, producers, balance.rstrip().replace(' ','')))
		print('%s,%s,%s' % (user, producers, balance.rstrip().replace(' ','')))
		#time.sleep(.5)
p.close()
e.close()
