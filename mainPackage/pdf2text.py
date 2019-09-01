'''
This module extract the text from a pdf file.
DISCLAIMER: Although this method works properly most of the times, sometimes
it gives slightly wrong directions due to pdf formatting issues. This is fixed
by using the email_curate script.
'''

from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io
from PyPDF2 import PdfFileReader
from progress.bar import ShadyBar


def pdf_conversion(filename):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(filename, 'rb') as fh:
        pdfObj = PdfFileReader(fh)
        num_pages = pdfObj.getNumPages()
        pages = PDFPage.get_pages(fh)
        bar = ShadyBar('Processing', max=num_pages, suffix='%(percent)d%%')
        for page in pages:
            page_interpreter.process_page(page)
            bar.next()

        bar.finish()
        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()
    return text
