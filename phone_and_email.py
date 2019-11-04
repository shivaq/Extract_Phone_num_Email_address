#! python3
# phone_and_email.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# Phone number regex
phone_regex = re.compile(r'''(
(\d{3}|\(\d{3}\))?          # optional area code 
(\s|-|\.)?                  # separator
(\d{3})                     # first 3 digits
(\s|-|\.)?                  # separator
(\d{4})                     # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2, 5}))? # extension
)''', re.VERBOSE)

# Email regex
email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+               # username
@                               # @ symbol
[a-zA-Z0-9.-]+                  # domain name
(\.[a-zA-Z]{2,4})               # dot-something
)''', re.VERBOSE)


def copy_clipboard():
    return str(pyperclip.paste())


def get_phone_nums_from_clipboard(text):
    num_matches = []

    for groups in phone_regex.findall(text):
        phone_num = '-'.join([groups[1], groups[3], groups[5]])

        if groups[8] != '':
            phone_num += ' x' + groups[8]

        num_matches.append(phone_num)

    return num_matches


def get_email_addresses_from_clipboard(text):
    address_matches = []
    for groups in email_regex.findall(text):
        address_matches.append(groups[0])

    return address_matches


def print_matched_phone_nums():
    num_matches = get_phone_nums_from_clipboard(copy_clipboard())
    if len(num_matches) > 0:
        pyperclip.copy('\n'.join(num_matches))
        print('Copied to clipboard:')
        print('\n'.join(num_matches))
    else:
        print('No phone numbers found.')


def print_matched_email_addresses():
    address_matches = get_email_addresses_from_clipboard(copy_clipboard())
    if len(address_matches) > 0:
        pyperclip.copy('\n'.join(address_matches))
        print('Copied to clipboard:')
        print('\n'.join(address_matches))
    else:
        print('No email addresses found.')


def print_matched_email_addresses_and_phone_nums():
    matches = get_email_addresses_from_clipboard(copy_clipboard()) + get_phone_nums_from_clipboard(copy_clipboard())
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')


# print_matched_phone_nums()

# print_matched_email_addresses()

print_matched_email_addresses_and_phone_nums()
