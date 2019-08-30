'''
This module will analyze each line_split to get a email addresses according to
the RFC 5322 criteria.
'''
import re


def email_analyze(str, emails):
    '''
    This function searches for all the valid emails within a given string.
    input: a given string.
    output: a list containing all the valid emails.
    '''
    # The following pattern matches the RFC 5322 criteria:
    regex = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
    str_emails = regex.findall(str)
    for email in str_emails:
        emails.append(email)
    return emails
