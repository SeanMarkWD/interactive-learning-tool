import random


class Question:
    # Description: Represents a single question, either multiple-choice or free-form text.

    # Attributes: 
    def __init__(self, question_id, question_text, correct_answer, possible_answers=None, active=None):
        # question ID
        self.question_id = question_id
        self._question_text = question_text
        # correct answer
        self.correct_answer = correct_answer
        # possible answers (for multiple-choice)
        self.possible_answers = possible_answers
        # active status (enabled/disabled)
        self.active = active
        # update statistics
        self.times_shown = 0
        self.times_answered_correctly = 0

    # Methods
    # Enable/disable
    def enable(self):
        self.active = True

    def disable(self):
        self.active = False

    # Check answer (compare user's answer with the correct one)
    def check_answer(self, user_answer):
        self.times_shown += 1
        if user_answer.lower() == self.correct_answer.lower():
            self.times_answered_correctly += 1
            return True
        return False
    
    # Getter for question_text
    @property
    def question_text(self):
        return self.question_text
    
    # Setter for question_text
    @question_text.setter
    def question_text(self, new_text):
        if not new_text.strip():
            raise ValueError("question_text cannot be empty")
        self._question_text = new_text

class QuestionBank:
    # Description: Handles a List or collection of Question object.
    #Attributes: 
    def __init__(self):
        self.questions = []

    # Methods: 
    # Add a question
    def add_question(self, question):
        self.questions.append(question)

    # Remove a question
    def remove_question(self, question_id):
        self.questions = [q for q in self.questions if q.question_id != question_id]

    # Fetch a question by ID
    def fetch_question_by_id(self, question_id):
        for question in self.questions:
            if question.question_id == question_id:
                return question
        return None

    # Enable/disable a question based on ID
    def enable_disable_question(self, question_id, enable=True):
        question = self.fetch_question_by_id(question_id)
        if question:
            if enable:
                question.enable()

    #Display statistics for all questions
    # statistics (times shown, times answered correctly).
    def display_statistics(self):
        for question in self.questions:
            print(f"ID: {question.question_id}, Shown: {question.times_shown}, Correct: {question.times_answered_correctly}")


class QuizManager:
# Description: Manages the logic for conducting a quiz or practice session, using questions from the QuestionBank.
# Attributes: 
    def __init__(self, question_bank):
        self.question_bank = question_bank
        # Current score
        self.current_score = 0
        # list of questions used in the session
        self.questions_used = []
        # number of questions (for a test), user's answers
        self.questions_answered = []

    # Starts a quiz
    def start_quiz(self):
        self.current_score = 0
        self.questions_used = []
        self.questions_answered = []
        self.select_next_question()

    # Select next question
    def select_next_question(self):
        # Randomly select a question not yet used
        remaining_questions = [q for q in self.question_bank.questions if q not in self.questions_used]
        if remaining_questions:
            next_question = random.choice(remaining_questions)
            self.questions_used.append(next_question)
            return next_question
        # No more questions available
        return None 
    
    # evaluates user's answer
    def evaluate_answer(self, question, user_answer):
        if question.check_answer(user_answer):
            self.current_score += 1
            # Record the question as answered correctly
            self.questions_answered.append(question, True)
        else:
            # Record the question as answered incorrectly
            self.questions_answered.append(question, False)

    def calculate_final_score(self):
        return self.current_score


# PracticeTestSession:

#Practice Mode

#Test Mode


# class UserProfile:
# NB! Requires validation so using Getters 
# and Setters the pythonic way is a 
# great opportunity here
'''
Attributes:
username: A unique identifier for the user. This could be their actual name or a chosen nickname.
email: The user's email address, used for account verification, notifications, and password resets.
password: A hashed password for login purposes. (Note: It's critical to handle passwords securely, usually storing only a hashed version rather than the plain text.)

Methods:
login(): Validates user credentials and allows access to their profile.
update_profile(info): Updates the user's profile information, where info could be a dictionary containing items like email, password, or preferences.
change_password(old_password, new_password): Allows the user to change their password, ensuring they provide the correct current password for security.
reset_progress(): Clears the user's progress and score history, starting over from scratch.
get_statistics(): Returns a summary of the user's performance and progress, such as average scores, most improved areas, or total time spent on the platform.
save(): Persists the user's current state, including updated profile information, progress, and preferences, to a file or database.
load(): Retrieves the user's profile information, preferences, and progress from storage.
'''

# class UserStatistics:
# Description: Tracks and manages statistics related to user performance.
"""
Attributes: 
Total questions answered, 
percentage of correct answers, 
score_history: A list or dictionary that tracks the user's scores on quizzes or tests over time.

Methods: 
Update statistics, 
display user's performance metrics.
"""

# class File Manager
# Description: Handles reading from and writing to files (questions, configurations, statistics).
"""
Attributes: File paths.

Methods: 
Load questions, 
save questions, 
load statistics, 
save statistics.
"""


# def Main():


# if __name == "__main__":
# Main()
