'''
This module finds the extension of the file selected by the user.
'''


def find_extension(filename):
    '''
    Finds the extension of a given file.
    input: filename
    output: file extension
    '''
    filename_list = filename.split('/')
    extension = filename_list[-1].split('.')[-1]
    return extension
