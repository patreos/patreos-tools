class CommandBuilder:
	def __init__(self, api='https://api.eosnewyork.io', cleos='/Users/okayplanet/dev/eos/eos/build/programs/cleos/cleos'):
		self.api = api
		self.cleos = cleos


	#cleos -u https://eos.greymass.com/ get scope patreostoken -t stakes -l 1
	def build_get_stake_table(self, limit, lower=None):
		if lower is None:
			return [
				'%s' % self.cleos,
				'--url',
				'%s' % self.api,
				'get',
				'scope',
				'patreostoken',
				'--table',
				'stakes',
				'--limit',
				'%s' % limit
			]
		return [
			'%s' % self.cleos,
			'--url',
			'%s' % self.api,
			'get',
			'scope',
			'patreostoken',
			'--table',
			'stakes',
			'--lower',
			' %s' % lower,
			'--limit',
			'%s' % limit
		]

	def build_get_voter_table(self, limit, lower=None):
		if lower is None:
			return [
				'%s' % self.cleos,
				'--url',
				'%s' % self.api,
				'get',
				'table',
				'eosio',
				'eosio',
				'voters',
				'--limit',
				'%s' % limit
			]
		return [
			'%s' % self.cleos,
			'--url',
			'%s' % self.api,
			'get',
			'table',
			'eosio',
			'eosio',
			'voters',
			'--lower',
			' %s' % lower,
			'--limit',
			'%s' % limit
		]

	def build_get_account(self, user):
		cmd = [
			'%s' % self.cleos,
			'--url',
			'%s' % self.api,
			'get',
			'account',
			'%s' % user
		]
		return cmd

	def grep(self, value, file):
		cmd = [
			'grep',
			'-m',
			'1',
			'%s' % value,
			'%s' % file
		]
		return cmd
