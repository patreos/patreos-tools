#!/usr/local/bin/python3.7

messages = {
    "NO_BALANCE_OBJECT": "No balance object found",
    "CANNOT_BLURB_TO_SELF": "cannot blurb to self",
    "TO_ACCCOUNT_DNE": "to account does not exist",
    "CREATOR_ACCOUNT_DNE": "Creator account does not exist",
    "PLEDGE_EXISTS": "Pledge already exists.",
    "UNSUPPORTED_TOKEN": "We do not support this token currently",
    "INVALID_QUANTITY": "Invalid quantity",
    "NEED_POSITIVE_PLEDGE_QUANTITY": "Must pledge positive quantity",
    "UNFOUND_TOKEN": "Token could not be found",
    "NEED_MIN_QUANTITY": "Must pledge at least min quanity",
    "INVALID_SYMBOL": "Symbol precision mismatch",
    "NO_VAULT_BALANCE": "You have no balance to pledge",
    "NEED_PLEDGE_FUNDS": "Insufficent funds for pledge amount",
    "NEED_LARGER_VAULT_BALANCE": "Expected a balance of 2x the pledge",
    "INVALID_CYCLE": "Invalid pledge cycle",
    "PLEDGE_DNE": "pledge does not exist.",
    "NEED_AUTH_FOR_UNPLEDGE": "Not authorized to unpledge",
    "OVERDRAWN_BALANCE": "overdrawn balance",
    "NEED_MIN_EOS_DEPOSIT": "Minimum deposit of 0.1 EOS required",
    "NEED_MIN_PATR_DEPOSIT": "Minimum deposit of 50 PTR required",
    "NEED_POSITIVE_TRANSFER_AMOUNT": "Cannot transfer non-positive amount",
    "NO_BALANCE_FOR_TOKEN": "No balance found for that token",
    "NO_BALANCE_OBJECT": "no balance object found",
    "TOKEN_CONTRACT_DNE": "Token contract could not be found",
    "NEED_AUTH_FOR_PROCESSING": "Not authorized to process this subscription",
    "PLEDGE_NOT_DUE": "Pledge subscription not due",
    "TOKEN_FEE_DNE": "Token fee could not be found",
    "INVALID_SYMBOL_NAME": "invalid symbol name",
    "INVALID_SUPPLY": "invalid supply",
    "NEED_POSITIVE_MAX_SUPPLY": "max-supply must be positive",
    "SYMBOL_EXISTS": "token with symbol already exists",
    "MEMO_TOO_LONG": "memo has more than 256 bytes",
    "TOKEN_DNE_YET": "token with symbol does not exist, create token before issue",
    "NEED_POSITIVE_ISSUE_QUANTITY": "must issue positive quantity",
    "EXCEEDS_SUPPLY": "quantity exceeds available supply",
    "TOKEN_DNE": "token with symbol does not exist",
    "NEED_POSITIVE_RETIRE_QUANTITY": "must retire positive quantity",
    "CANNOT_TRANSFER_TO_SELF": "cannot transfer to self",
    "ACCOUNT_DNE": "to account does not exist",
    "SYMBOL_DNE": "symbol does not exist",
    "CLOSE_BALANCE_NO_EFFECT": "Balance row already deleted or never existed. Action won't have any effect.",
    "CLOSE_BALANCE_NONZERO": "Cannot close because the balance is not zero.",
    "NEED_POSITIVE_TRANSFER_QUANTITY": "must transfer positive quantity",
    "NEED_POSITIVE_WITHDRAW_QUANTITY": "must withdraw positive quantity"
}

def get_python():
    print("// THIS IS A GENERATED FILE FROM PATREOS-TOOLS.  DO NOT CHANGE.")
    print("var messages = {")
    for key, value in messages.items():
        print(f"    {key}: \"{value}\",")
    print("}")
    print()
    print("module.exports.messages = messages;")

def get_c():
    print("// THIS IS A GENERATED FILE FROM PATREOS-TOOLS.  DO NOT CHANGE.")
    print("#pragma once")
    print()
    print("#include <string>")
    print()
    print("class Messages {")
    print("public:")
    for key, value in messages.items():
        print(f"    const static char* {key};")
    print("};")
    for key, value in messages.items():
        print(f"const char* Messages::{key} = \"{value}\";")

get_python()
print()
get_c()
