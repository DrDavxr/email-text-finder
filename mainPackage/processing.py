'''
This module will analyze each line_split to get a email addresses according to
the RFC 5322 criteria.
'''
import re


def email_analyze(lines):
    emails = []
    find_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    for line in lines:
        line_emails = re.findall(find_pattern, line)
        for email in line_emails:
            emails.append(email)
    return emails
