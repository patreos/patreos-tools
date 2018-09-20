import subprocess
import datetime
import sys
from commons import Commons
from command_builder import CommandBuilder

commons = Commons()
command_builder = CommandBuilder()
today = datetime.datetime.now().strftime("%Y-%m-%d")
today = '2018-08-30'
missing = open('./data/voter_coverage_check_%s.txt' % today, 'w')

count = 0
with open('./data/voter_accounts_%s.txt' % today, 'r') as f:
	print('opened')
	for line in f:

		if commons.is_blank(line.rstrip()):
			continue

		tokens = commons.safe_split(line.rstrip(), ',', 2)
		user = tokens[0]
		if commons.is_blank(user):
			continue

		cmd = command_builder.grep(user, './data/voter_balances_%s.txt' % today)
		match = commons.cmd_exec(cmd)
		if match is None:
			print("WARNING: %s unaccounted for" % user)
			missing.write('%s\n' % user)
			missing.flush()
			count = count + 1
			continue

		user_field = commons.safe_split(match, ',', 3)[0]
		if commons.is_blank(user_field) or user_field != user:
			print("WARNING: %s unaccounted for" % user)
			missing.write('%s\n' % user)
			missing.flush()
			count = count + 1
			continue

		print("%s accounted for!" % user)

missing.close()
print("Finished.  Found %s missing users" % count)
