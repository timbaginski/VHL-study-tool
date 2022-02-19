import sys
import argparse
import pdf_parser
import studymanager


def main():
    parser = argparse.ArgumentParser(description="create a study set")
    parser.add_argument('-t', action='store_const', const=True, 
    help='Answer with term instead of definition')
    parser.add_argument('path', help='path of study sheet PDF')

    args = parser.parse_args()


main()
