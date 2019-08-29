'''
This is a simple script that will search for email addresses given a text file,
according to the RFC 5322 validation standard.
'''

from mainPackage import file_manipulation, file_request, email_validation


def main():
    filename = file_request.file_req()
    file = file_manipulation.File(filename)
    # Open the file.
    lines = file.open_file()
    print(file)
    emails = set(email_validation.email_analyze(lines))
    print(f'A total amount of {len(emails)} emails were found:')
    print('---------------------------------------------')
    for email in emails:
        print(email)


if __name__ == '__main__':
    main()
