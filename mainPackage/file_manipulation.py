'''
This module contains all the code related with the manipulation of file(s).
'''
import sys
from mainPackage import email_validation


class File():

    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return "Opening file '{file}' ... \n".format(file=self.filename)

    def file_processing(self, emails):
        '''
        Function that opens an specific file.
        '''
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    emails = email_validation.email_analyze(line, emails)
            return emails
        except FileNotFoundError:
            sys.exit("FILE WAS NOT SELECTED OR FOUND!")
