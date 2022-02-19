import pdfplumber 
from itertools import filterfalse


def clear_invalid_lines(l):
    for item in l:
        if any(map(str.isdigit, item)):
            return True
    return len(l) != 2


def clean_row(x):
    return x == None or x == ''


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


def parse_pdf(path):
    pdf = pdfplumber.open(path)
    return get_lines(pdf)

    
   
                               


