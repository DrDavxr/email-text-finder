'''
This module contains all the code related with the manipulation of file(s).
'''
import sys


class File():

    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return "Opening file '{file}' ... \n".format(file=self.file_name)

    def open_file(self):
        '''
        Function that opens an specific file.
        '''
        try:
            with open(self.file_name, 'r') as f:
                self.lines = f.readlines()  # list containing all the lines.
                f.close()
        except FileNotFoundError:
            sys.exit("FILE WAS NOT SELECTED OR FOUND!")
        return self.lines  # Returns a list with all the lines.
