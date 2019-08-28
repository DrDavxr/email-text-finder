'''
Module that includes the script related with the file(s) request. For the
moment, only one file is read, and is previously defined in the code.
'''

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os


def file_req():
    # Avoids the root window from appearing.
    Tk().withdraw()
    # Show an "Open" dialog box and return the path to the selected file
    filename = askopenfilename(initialdir=os.getcwd(),
                               title="Select file...",
                               filetypes=(("Text files", "*.txt"),
                                          ("all files", "*.*")))
    return filename
