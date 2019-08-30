'''
This module contains all the code related with the manipulation of file(s).
'''
import sys
from mainPackage import email_validation, pdf2text
import tkinter
from tkinter import messagebox
from progress.bar import ShadyBar


class File():

    def __init__(self, filename, extension):
        self.filename = filename
        self.extension = extension

    def __str__(self):
        return "Opening file '{file}' ... \n".format(file=self.filename)

    def file_processing(self, emails):
        '''
        Function that opens an specific file
        input: an empty list where the emails will be stored.
        output: a list containing all the emails found.
        '''
        try:
            if self.extension == 'txt':
                with open(self.filename, 'r') as f:
                    num_lines = sum(1 for line in f if line.rstrip())
                    f.seek(0)
                    bar = ShadyBar('Processing', max=num_lines,
                                   suffix='%(percent)d%%')
                    for line in f:
                        emails = email_validation.email_analyze(line, emails)
                        bar.next()
                    bar.finish()
                    f.close()
                return emails
            elif self.extension == 'pdf':
                text = pdf2text.pdf_conversion(self.filename)
                emails = email_validation.email_analyze(text, emails)
                return emails
            else:
                # Hide main window:
                root = tkinter.Tk()
                root.withdraw()
                # Error display
                error_message = \
                    f'The "{self.extension}" extension cannot be opened!'
                messagebox.showerror("Error", error_message)
                # Abort the execution of the program
                sys.exit()
        except FileNotFoundError:
            sys.exit("FILE WAS NOT SELECTED OR FOUND!")
