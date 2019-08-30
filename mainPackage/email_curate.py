'''
This module cleans the obtained emails obtained from PDFs files, where the
conversion to text sometimes yields wrong directions. The principle in which
this module is based off is the fact that after the .com (or similar), no
numbers nor uppercase letters appear.

'''
import re


def email_cleaner(emails):
    '''
    This function gets the set of all the detected emails and cleans them
    to get a ready-to-use email direction.
    input: set of all the emails.
    output: list containing the clean emails.
    '''
    clean_emails = []
    for email in emails:
        domain = ''
        last_domain_part = ''
        # Split the direction into two parts with @.
        raw_list = re.split('@', email)
        # Split the second part of the previous list by using '.' pattern.
        raw_domain = raw_list[1].split('.')
        # The user is the part before the @.
        user = raw_list[0]
        for domain_part in raw_domain:
            # The last item in raw_domain is the one which usually has wrong
            # items.
            if domain_part == raw_domain[-1]:
                for letter in domain_part:
                    if letter.isupper() or letter.isdigit():
                        break
                    else:
                        last_domain_part += letter
                domain += last_domain_part
            else:
                domain = domain + domain_part + '.'
        clean_email = user + '@' + domain
        clean_emails.append(clean_email)
    return clean_emails
