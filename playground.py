from commons import Commons
from command_builder import CommandBuilder
import subprocess
import json
import sys

commons = Commons()
command_builder = CommandBuilder()

cmd = command_builder.build_get_voter_table(5, 'b1')
json = commons.get_correct_json_from_cmd(cmd, 'rows')
print(json)

cmd = command_builder.build_get_account('b1')
ret = commons.get_correct_account_response_from_cmd(cmd, 'total')
if ret is None:
    print("Problem with getting account balance")
else:
    print("Account balance is: %s" % ret)

cmd = command_builder.build_get_account('patreosxxxxx')
ret = commons.get_correct_account_response_from_cmd(cmd, 'total')
if ret is None:
    print("Problem with cmd: `%s`" % (' '.join(cmd)), file=sys.stderr)
else:
    print("Account balance is: %s" % ret)


tokens = commons.safe_split("patreosxxxxx,20", ',', 2)
print(tokens[0])


cmd = command_builder.build_get_voter_table(1)
print(' '.join(cmd))
