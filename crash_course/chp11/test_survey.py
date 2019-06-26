# coding: utf-8
import unittest

from crash_course.chp11.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = 'ww'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['english', 'chinese', 'jpn']

    def test_store_single_response1(self):
        self.my_survey.store_response(self.responses[0], self.my_survey.response)
        self.assertIn(self.responses[0], self.my_survey.response)

    def test_store_three_response1(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

    def test_store_single_response(self):
        question = "w s"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('english')
        self.assertIn('english', my_survey.responses)

    def test_store_three_response(self):
        question = "w s"
        responses = ['english', 'chinese', 'jpn']
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('english')
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()
