import sys
import argparse
import pdf_parser
from studymanager import StudyManager


# purpose: ask user whether they would like to override an incorrect answer
# inputs: StudyManager
# returns: boolean representing whether the user decided to override
def ask_for_override(manager):
    override = input(f"Incorrect. Answer was {manager.get_answer()}. Override? (y/n)")
    return override[0] == 'y'


# purpose: run the study session 
# inputs: study manager, which will run the session
def launch_session(manager):
    while not manager.is_finished():
        answer = input(manager.get_prompt())
        is_correct = manager.matches_prompt(answer)
        if is_correct:
            print("Correct!")
        else:
            is_correct = ask_for_override(manager)
        
        manager.advance_line(is_correct)

    print("Session finished")


def main():
    parser = argparse.ArgumentParser(description="create a study set")
    parser.add_argument('-t', dest='answer_with_term', action='store_const', const=True, default=False,
    help='Answer with term instead of definition')
    parser.add_argument('path', help='path of study sheet PDF')

    args = parser.parse_args()
    lines = pdf_parser.parse_pdf(args.path)
    manager = StudyManager(lines, args.answer_with_term)

    launch_session(manager)

            
if __name__ == '__main__':
    main()
