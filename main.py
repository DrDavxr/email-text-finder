'''
This is the main script that will search for email addresses given an accepted
file, according to the RFC 5322 validation standard.
'''

from mainPackage import file_manipulation, file_request, extension_detector
from mainPackage import email_curate


def main():
    emails = []
    filename = file_request.file_req()
    extension = extension_detector.find_extension(filename)
    file = file_manipulation.File(filename, extension)
    print(file)
    emails = set(file.file_processing(emails))
    if extension == 'pdf':
        emails = email_curate.email_cleaner(emails)
    else:
        pass
    print(f'A total amount of {len(emails)} emails were found:')
    print('---------------------------------------------')
    for email in emails:
        print(email)
    print('---------------------------------------------')


if __name__ == '__main__':
    main()
