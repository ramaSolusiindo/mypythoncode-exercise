import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """ Test for the class AnonymousSurvey """
    def test_store_single_response(self):
        """ Test that a single response is stored properly. """
        question = "What language did you first learn to speak? "
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.response)

    def test_store_three_responses(self):
        """ Test that three individual responses are stored properly. """
        question = "What language did you first learn to speak? "
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for resp in responses:
            my_survey.store_response(resp)

        for resp in responses:
            self.assertIn(resp, my_survey.response)

    if __name__ == '__main__':
        unittest.main