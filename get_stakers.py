import json
import subprocess
import time
from pprint import pprint
import datetime
from commons import Commons
from command_builder import CommandBuilder

today = datetime.datetime.now().strftime("%Y-%m-%d")
#today = '2018-08-30'
step_size = 100
debug = True
commons = Commons()
command_builder = CommandBuilder()

cmd = command_builder.build_get_stake_table(1)
first_record = commons.get_correct_json_from_cmd(cmd, 'rows', False)

user = first_record['rows'][0]['scope']
old_user = ''
f = open('./data/staker_accounts_%s.txt' % today, 'w')
pprint("Starting with staker: %s" % user)

f.write('%s\n' % user)

while user != old_user:
	cmd = command_builder.build_get_stake_table(step_size, user)
	json_result = commons.get_correct_json_from_cmd(cmd, 'rows')
	if json_result is None:
		raise ValueError('Could not get valid json response for user: %s!' % user)

	old_user = user
	for row in json_result['rows']:
		user = row['scope']
		if(user == old_user):
			print("Done...")
			continue;

		if debug:
			pprint('%s' % row['scope'])


		f.write('%s\n' % row['scope'])

	if user == old_user:
		print("Done")
		break;
	#time.sleep(2)   # Delays for 5 seconds. You can also use a float value.
f.close()
