# coding: utf-8
from crash_course.chp11.survey import AnonymousSurvey

question = "what speaking"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("q quit")
while True:
    response = input("lan:")
    if (response == 'q'):
        break
    my_survey.store_response(response)
