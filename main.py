from re import S
import sys
import argparse
import pdf_parser
from studymanager import StudyManager


def main():
    parser = argparse.ArgumentParser(description="create a study set")
    parser.add_argument('-t', dest='answer_with_term', action='store_const', const=True, default=False,
    help='Answer with term instead of definition')
    parser.add_argument('path', help='path of study sheet PDF')

    args = parser.parse_args()
    lines = pdf_parser.parse_pdf(args.path)
    print(args.answer_with_term)
    study_manager = StudyManager(lines, args.answer_with_term)


main()
