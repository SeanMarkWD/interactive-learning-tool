from main import Question


def main():
    test_check_correct_answer()
    test_check_incorrect_answer()
    test_is_correct_case_insensitive()
    test_enable_disable_questions()

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


if __name__ == "__main__":
    main()