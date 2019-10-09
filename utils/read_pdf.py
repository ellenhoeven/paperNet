import io

from pdfminer.converter import TextConverter, XMLConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams


def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a pdf document

    Parameters: pdf_path (string) of where the document is located

    Returns: text (string)
    """
    resource_manager = PDFResourceManager()
    fake_file_handle = io.BytesIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text


def pdfparser(path):
    """
    Parses text from a pdf document

    Parameters: path (string) of where the document is located

    Returns: text (string)
    """
    fp = open(path, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        text = retstr.getvalue()
    return text
