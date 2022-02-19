import pdfplumber 
from itertools import filterfalse


def is_valid(l):
    for item in l:
        if any(map(str.isdigit, item)):
            return True
    return False or (len(l) != 2)


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
    lines[:] = filterfalse(is_valid, lines)
    return lines


def main():
    pdf = pdfplumber.open('vocab.pdf')
    lines = get_lines(pdf)

    for line in lines:
        print(str(line) + '\n')
   
                               
main()


