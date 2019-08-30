'''
Module that includes the script related with the file(s) request. For the
moment, only one file is read, and is previously defined in the code.
'''

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os


def file_req():
    '''
    Opens a dialog box so the user can choose the desired file.
    no input required.
    output: the full file path.
    '''
    # Avoids the root window from appearing.
    Tk().withdraw()
    # Show an "Open" dialog box and return the path to the selected file
    filename = askopenfilename(initialdir=os.getcwd(),
                               title="Select file...",
                               filetypes=(("Text files (.txt)", "*.txt"),
                                          ("PDF Files (.pdf)", "*.pdf"),
                                          ("All files (*.*)", "*.*")))
    return filename
