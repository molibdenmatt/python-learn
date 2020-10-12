from survey import AnonymousSurvey

question = "What is your native language?"
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print("type 'q' to end the survey.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("Thank You for the survey!")
my_survey.show_results()