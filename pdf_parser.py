import pdfplumber 
from itertools import filterfalse


'''
purpose: clear any lines that contain erroneous information or don't contain two items
This filters out the heading attop each page as well as date/time info
returns: use with filterfalse: True when invalid, False when valid
'''
def clear_invalid_lines(l):
    for item in l:
        if any(map(str.isdigit, item)):
            return True
    return len(l) != 2


'''
purpose: Remove leading/trailing None/empty items from row
returns: use with filterfalse: True when item is invalid, False when valid 
'''
def clean_row(x):
    return x == None or x == ''


'''
purpose: takes a pdf object, returns a list of terms/definitions
returns: "lines" a list of terms/definition pairs
'''
def get_lines(pdf):
    lines = []
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                row[:] = filterfalse(clean_row, row)
                lines.append(row)
    lines[:] = filterfalse(clear_invalid_lines, lines)
    return lines


'''
purpose: given a file path, open a pdf and retrieve its lines (term/definition pairs)
returns: the lines of the given pdf
'''
def parse_pdf(path):
    pdf = pdfplumber.open(path)
    return get_lines(pdf)

    
   
                               


