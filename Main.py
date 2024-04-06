class Question:
    # Description: Represents a single question, either multiple-choice or free-form text.

    # Attributes: 
    def __init__(self, question_id, question_text, correct_answer, possible_answers=None, active=None):
        # question ID
        self.question_id = question_id
        self.question_text = question_text
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
    # enable/disable
    def enable(self):
        self.active = True

    def disable(self):
        self.active = False

    # check answer (compare user's answer with the correct one)
    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()


# class QuestionBank:
# Description: Handles a collection of questions.
"""
Attributes: 
List or collection of Question objects.
Methods: 
add a question, 
remove a question, 
fetch a question by ID, 
enable/disable a question based on ID, 
"""

#Statistics Viewing
# statistics (times shown, times answered correctly).
"""
Method:
display statistics for all questions.
"""


# class QuizManager:
# Description: Manages the logic for conducting a quiz or practice session, using questions from the QuestionBank.
"""
Attributes: 
Current score, 
list of questions used in the session, 
number of questions (for a test), user's answers.

Methods: 
Start quiz/test, 
select next question (randomly or based on criteria for practice), 
evaluate answer, 
calculate final score.
"""

# PracticeTestSession:

#Practice Mode

#Test Mode


# class UserProfile:
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
