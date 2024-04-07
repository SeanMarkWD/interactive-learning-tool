import random
import hashlib


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


class UserProfile:
# NB! Requires validation so using Getters 
    # NB! Requires validation so using Getters 
# and Setters the pythonic way is a 
# great opportunity here

    # Attributes:
    def __init__(self, username, email, age, password):
        # A unique identifier for the user. 
        # Could be their actual name or a chosen nickname.
        self.username = username
        # used for account verification, notifications, and password resets.
        self._email = email
        self._age = age
        # Hashed password for login purposes.
        # (Note: It's critical to handle passwords securely
        self.password = self.hash_password(password)
        self.score_history = {}
        self.progress = {}

    # Methods:
    def login(self, username, password):
        #  Validates user credentials and allows access to their profile.
        hashed_password = self.hash_password(password)
        if self.username == username and self.password == hashed_password:
            print("Login successful!")
        else:
            print("Invalid username or password.")

    def update_profile(self, info):
        # Updates the user's profile information, where info 
        # could be a dictionary containing items like email, 
        # password, or maybe preferences.
        if "email" in info:
            self.email = info["email"]
        if "password" in info:
            self.password = self.hash_password(info["password"])
        print("Profile updated.")  

    def change_password(self, old_password, new_password):
        # Allows the user to change their password, ensuring 
        # they provide the correct current password for security.
        if self.password == self.hash_password(old_password):
            self.password = self.hash_password(new_password)
            print("Password changed successfully. ")
        else:
            print("The old password is incorrect. ")

    def reset_progress(self):
        # Clears the user's progress and score history, starting over from scratch.
        self.score_history = {}
        self.progress = {}
        print("Progress has been reset. ")

    def get_statistics(self):
        # Example: Return count of completed tasks
        tasks_completed = len(self.progress)
        print(f"Tasks completed: {tasks_completed}")
        # Examples for further development include:
        # Returns a summary of the user's performance and progress, 
        # such as average scores, most improved areas, 
        # or total time spent on the platform.

    def save(self):
        # Save user profile to file or database, including 
        # updated profile information, progress, and preferences.
        pass

    def loaf():
        # Retrieves the user's profile information, 
        # preferences, and progress from storage.
        pass

    def hash_password(self, password):
        # Return a hashed version of the password
        # Simple hashing using SHA-256.
        hashed = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return hashed


    # Email getter
    @property
    def email(self):
        return self._email
    
    # Email setter with basic validation
    @email.setter
    def email(self, new_email):
        if "@" not in new_email or "." not in new_email:
            raise ValueError("This i not a valid email address.")
        self._email = new_email

    # Age getter
    @property
    def age(self):
        return self._age
    
    # Age setter with validation
    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int) or new_age <= 0:
            raise ValueError("Age must be positive integer.")
        self._age = new_age


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


def main():
    pass


if __name__ == "__main__":
    main()

    """
    user = UserProfile(username="john_doe", email="john.doe@example.com", age=30, password="securepassword123")
    
    # Accessing attributes through getters
    print(user.email)
    print(user.age)
    
    # Updating attributes through setters
    user.email = "new_email@example.com"
    user.age = 25
    
    # Attempting to set invalid values
    try:
        user.email = "invalid_email"
    except ValueError as e:
        print(e)

    try:
        user.age = -5
    except ValueError as e:
        print(e)
    """
