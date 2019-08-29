'''
This is a simple script that will search for email addresses given a text file,
according to the RFC 5322 validation standard.
'''

from mainPackage import file_manipulation, file_request


def main():
    emails = []
    filename = file_request.file_req()
    file = file_manipulation.File(filename)
    # Open the file.
    emails = set(file.file_processing(emails))
    print(file)
    print(f'A total amount of {len(emails)} emails were found:')
    print('---------------------------------------------')
    for email in emails:
        print(email)


if __name__ == '__main__':
    main()
