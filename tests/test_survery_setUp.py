import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvery(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    def setUp(self) -> None:
        """
        Create a sruvery and set of response sfor sue in all test methods"""

        question = "What language di you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
if __name__ == '__main__':
    unittest.main()