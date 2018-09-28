import subprocess
import time
import re
import datetime
from decimal import Decimal
from colors import Colors
from commons import Commons
import math

commons = Commons()
color = Colors()
fg = color.fg()
today = datetime.datetime.now().strftime("%Y-%m-%d")
today = '2018-09-27'

def cyan(stmt):
	return fg.lightcyan + str(stmt) + color.reset

def purple(stmt):
	return fg.purple + str(stmt) + color.reset

def yellow(stmt):
	return fg.yellow + str(stmt) + color.reset

total_supply = Decimal(2000000000)
airdrop_supply = Decimal(1200000000)
max_drop_ratio = Decimal(20)
user_base_cap_eos = 10000
#voter_number = 23890
ram_cost_eos_per_kb = 0.1195
ram_per_account_kb = 0.23
amounts = []
exchanges = [
	"haztmmbsguge", #chaince
	"haztmmbsgyge", #chaince
	"ha2tmmjygige" #chaince
]

def adjusted_drop_ratio(producers):
	bump = 14
	target = 20
	if int(producers) <= 3:
		return Decimal(2)
	if(int(producers) > 3 and int(producers) < 15):
		return Decimal(producers)/30 * max_drop_ratio * Decimal(math.atan(producers)) / Decimal(math.pi/2) + 1
	if(int(producers) >=15 and int(producers) < 30):
		return Decimal(bump) + Decimal( (target - bump) / (30 - 15) ) * Decimal( int(producers) - 15)
	if int(producers) == 30:
		return Decimal(target)

def adjusted_drop_cap(producers):
	bump = 133000
	target = 155000
	if int(producers) <= 3:
		return Decimal(user_base_cap_eos)
	if(int(producers) > 3 and int(producers) < 15):
		return user_base_cap_eos + 40 * user_base_cap_eos * Decimal(math.atan(1/40 * producers)) / Decimal(math.pi/2)
	if(int(producers) >=15 and int(producers) < 30):
		return Decimal(bump) + Decimal( (target - bump) / (30 - 15) ) * Decimal( int(producers) - 15)
	if int(producers) == 30:
		return Decimal(target)

amt = Decimal(0)
dropped = Decimal(0)
voter_number = 0
with open('./data/voter_balances_%s.txt' % today, 'r') as f:
	for line in f:
		line = line.rstrip()
		if commons.is_blank(line):
			continue

		#print(user_balance)
		tokens = commons.safe_split(line, ',', 3)
		user = tokens[0]
		producers = tokens[1]
		balance = tokens[2]

		user_cap_eos = adjusted_drop_cap(int(producers))
		if Decimal(balance) > Decimal(user_cap_eos):
			if user not in exchanges:
				balance = user_cap_eos
			else:
				print("Exchange %s with %s EOS" % (user, balance))
		amt = amt + Decimal(balance)
		dropped = dropped + Decimal(balance) * adjusted_drop_ratio(int(producers))
		amounts.append(Decimal(balance))
		voter_number = voter_number + 1

amounts = sorted(amounts)
for i in range(30):
	print("Vote %s Producer, Ratio is %s : 1 EOS" % (i + 1, '{0:.2f}'.format(adjusted_drop_ratio(i + 1))))
print('')
for i in range(30):
	print("Votes %s Producer, Cap is %s EOS" % (i + 1, '{0:.2f}'.format(adjusted_drop_cap(i + 1))))
print('')

print(purple("\n**** Airdrop Model Results ****"))
print("Gathered %s voters" % '{0:,}'.format(voter_number))
drop_percent = airdrop_supply / total_supply * 100
print("Dropping %s of %s (%s Percent)" % (cyan('{0:,}'.format(airdrop_supply) + ' PTR'), cyan('{0:,}'.format(total_supply) + ' PTR'), '{0:,}'.format(drop_percent)))
print("Aggregate total balance of %s EOS for all %s voters" % (amt, '{0:,}'.format(voter_number)))

total_drop = Decimal('{0:.4f}'.format(dropped))
print("Total airdrop ammount of %s accross all %s voters" % (cyan('{0:,}'.format(total_drop) + ' PTR'), '{0:,}'.format(voter_number)))
drop = airdrop_supply / amt
print("Estimated drop rate is %s to 1 EOS" % (cyan('{0:.4f}'.format(drop) + ' PTR')))
avg_eos = amt / voter_number
print("Average balance of %s EOS per %s voters" % ('{0:.4f}'.format(avg_eos), '{0:,}'.format(voter_number)))
avg_ptr = drop * avg_eos
print("Average drop balance of %s per %s voters" % (cyan('{0:.4f}'.format(avg_ptr) + ' PTR'), '{0:,}'.format(voter_number)))

median = amounts[int(len(amounts) / 2)]
print("Median balance of %s EOS per %s voters" % ('{0:.4f}'.format(median), '{0:,}'.format(voter_number)))
print("Median drop balance of %s per %s voters" % (cyan('{0:.4f}'.format(drop * median) + ' PTR'), '{0:,}'.format(voter_number)))
ram_needed = ram_per_account_kb * voter_number
eos_needed = ram_per_account_kb * voter_number * ram_cost_eos_per_kb
print("Estimated %s of RAM needed, %s EOS at market rate of %s EOS/kb" % (yellow('{0:.2f}'.format(ram_needed) + ' kb'), '{0:.4f}'.format(eos_needed), str(ram_cost_eos_per_kb)))
print(purple("*******************************\n"))
