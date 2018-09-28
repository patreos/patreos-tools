import subprocess
import json
import time
import re
import sys

class Commons:
    def __init__(self):
        self.x = ""

    # Not only must it be json, but must have specified key
    def is_correct_json(self, myjson, key):
        try:
            ret = json.loads(myjson)
            if key in ret:
                return True
            else:
                return False
        except (ValueError) as err:
            return False
        return True

    # Execute cmd, and receive correctly formatted json object
    def get_correct_json_from_cmd(self, cmd, key, debug=False):
        if debug:
            print(' '.join(cmd))
        count = 0
        while count < 5:
            result = subprocess.run(cmd, stdout=subprocess.PIPE)
            result = result.stdout.decode('utf-8')
            if self.is_correct_json(result, key):
                return json.loads(result)
            else:
                count = count + 1
                time.sleep(2)
        return None
        #raise ValueError('Could not get valid json response!')

    def is_correct_account_response(self, result, field):
        pattern = re.compile('%s:\s\s\s\s\s.*' % field) #total
        match = pattern.findall(result)
        if self.is_blank(match) or len(match) <= 0:
            return False
        else:
            return True

    # Execute cmd, and receive correctly formatted json object
    def get_correct_account_response_from_cmd(self, cmd, field, debug=False):
        if debug:
            print(' '.join(cmd))
        count = 0
        while count < 5:
            try:
                result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                result = result.stdout.decode('utf-8')
                if self.is_blank(result) or 'Failed with error' in result:
                    count = count + 1
                    if debug:
                        print("Cmd: %s returned bad result of: %s" % (' '.join(cmd), result), file=sys.stderr)
                    continue
            except (ValueError) as err:
                count = count + 1
                continue
            if self.is_correct_account_response(result, field):
                pattern = re.compile('%s:\s\s\s\s\s.*' % field)
                return pattern.findall(result)[0].replace('%s:' % field, '').rstrip().replace('EOS', '').replace(' ','')
            else:
                count = count + 1
                time.sleep(2)
        return None
        #raise ValueError('Could not get valid json response!')

    def cmd_exec(self, cmd):
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8').rstrip()
        if self.is_blank(result):
            return None
        return result

    # Apache utils mock
    def is_blank(self, str):
        if str == '' or str == None:
            return True
        else:
            return False

    # I want my splits to have an expected number of tokens
    def safe_split(self, str, char, expected_num_of_tokens):
        if char in str:
            tokens = str.split(char)
            if len(tokens) != expected_num_of_tokens:
                raise ValueError("Split on string: %s with character: %s did not result in %s tokens" % (str, char, expected_num_of_tokens))
            return tokens
        else:
            raise ValueError("Invalid split attempt to string: %s with character: %s" % (str, char))


    def safe_split_limit(self, str, char, tokens_limit):
        if char in str:
            tokens = str.split(char, tokens_limit - 1)
            if len(tokens) != tokens_limit:
                raise ValueError("Split on string: %s with character: %s did not result in %s tokens" % (str, char, tokens_limit))
            return tokens
        else:
            raise ValueError("Invalid split attempt to string: %s with character: %s" % (str, char))
