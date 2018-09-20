class CommandBuilder:
	def __init__(self, api='https://api.eosnewyork.io', cleos='/home/okayplanet/dev/eos/eos/build/programs/cleos/cleos'):
		self.api = api
		self.cleos = cleos

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
