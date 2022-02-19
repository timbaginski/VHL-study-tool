import itertools

class StudyManager:

    # purpose: initializes StudyManager by giving it lines, whether to answer with term or definition
    def __init__(self, lines, answer_with_term):
        self.lines = lines
        self.answer_index = 0 if answer_with_term else 1
        self.prompt_index = 1 if answer_with_term else 0
        self.line_index = 0 
        self.correct_count = list(itertools.repeat(0, len(lines)))


    # purpose: generate prompt from question_index and answer_with_term
    # returns: str representing the question prompt
    def get_prompt(self):
        return self.lines[self.line_index][self.prompt_index] 

    
    # purpose: obtain the answer for the current question
    # returns: str representing the answer
    def get_answer(self):
        return self.lines[self.line_index][self.answer_index]


    # purpose: determine whether a given answer matches the prompt
    # returns: True if it matches the prompt, False otherwise
    def matches_prompt(self, answer):
        return answer == self.lines[self.line_index][self.answer_index]

    
    # purpose: removes the lines at current index from lines and correct_count
    def remove_current_index(self):
        del self.lines[self.line_index]
        del self.correct_count[self.line_index]
        self.line_index -= 1


    # purpose: increment the correct count of an index if answer is correct
    # remove question from lines if it has been answered correctly twice
    def answer_correctly(self):
        if self.correct_count[self.line_index] == 2:
            self.remove_current_index()
        else:
            self.correct_count[self.line_index] += 1
        

    # purpose: advance the line index and based on user answer. If index equals 9, we return to zero
    # update correct_count if answer is correct
    def advance_line(self, is_correct):
        if is_correct:
            self.answer_correctly()
        end_index = min(9, len(self.lines) - 1)
        self.line_index = self.line_index + 1 if self.line_index < end_index else 0


    # purpose: returns whether the study session is finished (len(lines) == 0)
    # returns: boolean whether study session is finished
    def is_finished(self):
        return len(self.lines) == 0

        
            





    