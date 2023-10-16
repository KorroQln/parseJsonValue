import json

# Read the JSON data from a file
with open('sample.json', 'r') as file:
    data = json.load(file)

# Iterate through sections and questions to print reference, question, and OpenAnswer
for section in data['section']:
    for question in section['sectionQuestions']:
        reference = question['question']['reference']
        question_text = question['question']['question']
        open_answer = question['question']['response']['OpenAnswer']
        print("Reference:", reference)
        print("Question:", question_text)
        print("OpenAnswer:", open_answer)
        print()
        
print("DONE!")