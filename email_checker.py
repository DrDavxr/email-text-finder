'''
This is a simple script that will seek for email addresses given a text file.
'''

import re
import time


def main():
    start = time.time()
    split_term = '@'
    domain_patterns = {'gmail.com',
                       'hotmail.com',
                       'outlook.com',
                       'yahoo.com',
                       'alumnos.uc3m.es'}
    emails = []
    with open('data files/test_file_1.txt', 'r') as f:
        lines = f.readlines()  # list containing all the lines of a text
        f.close()
        for line in lines:
            line_list = re.split(split_term, line)
            for i in range(len(line_list)):
                if i == len(line_list)-1:
                    break
                else:
                    line_list_1 = line_list[i].split()
                    # print(line_list_1)
                    line_list_2 = line_list[i+1].split()
                    # print(line_list_2)
                    for domain_pattern in domain_patterns:
                        if re.match(domain_pattern, line_list_2[0]):
                            emails.append(line_list_1[-1] + '@' +
                                          line_list_2[0])
                        else:
                            continue
        emails = set(emails)  # To avoid repeated emails.
    for email in emails:
        print(email)
    end = time.time()
    delay = end-start
    print(f'Total time elapsed: {delay:{1}.{10}}')


if __name__ == '__main__':
    main()
