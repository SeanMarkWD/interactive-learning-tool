import pytest
from main import Question, QuestionBank
from unittest.mock import MagicMock


@pytest.fixture
def question_bank():
    # Create an instance of QuestionBank
    return QuestionBank()


def test_check_correct_answer():
    question = Question("1", "What is the capital of France?", "Paris")
    assert question.check_answer("Paris"), "Should return True for correct answer."


def test_check_incorrect_answer():
    question = Question("2", "What is the capital of France?", "Paris")
    assert not question.check_answer("Lyon"), "Should return False for incorrect answer."


def test_is_correct_case_insensitive():
    question = Question("3", "What is the capital of France?", "Paris")
    assert question.check_answer("paris"), "The method should return True for a case-insensitive match."


def test_enable_disable_questions():
    # tests if questions are enabled / disabled
    question = Question("4", "Is Python a programming language?", "Yes")
    question.disable()
    assert not question.active, "Question should be disabled."
    question.enable()
    assert question.active, "Question should be ensabled."
    print("Enable/disable test passed!")


def test_add_question(question_bank):
    question = MagicMock()
    question_bank.add_question(question)
    assert question in question_bank.questions

