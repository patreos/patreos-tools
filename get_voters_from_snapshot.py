import subprocess

snapshot_voters = open('./data/snapshot_voters.txt', 'w')
with open('./data/snapshot_users.txt', 'r') as f:
	for line in f:
		if line.rstrip() == '':
			continue;

		user = line.rstrip()
		cmd = [
			'grep',
			'%s' % user,
			'./data/voter_accounts_2018-08-30.txt'
		]

		result = subprocess.run(cmd, stdout=subprocess.PIPE)
		result = result.stdout.decode('utf-8').rstrip()
		if result != '' and result == user:
			print("%s voted!" % user)
			snapshot_voters.write('%s\n' % user)
		else:
			print("%s didn't vote" % user)
snapshot_voters.close()
