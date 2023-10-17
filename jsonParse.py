import json
from datetime import datetime

# Input string in ISO 8601 format
def format_iso8601(input_str):
    # Remove the "Z" and parse the ISO 8601 string
    input_str = input_str[:-1]  # Remove the "Z" at the end
    iso8601_datetime = datetime.fromisoformat(input_str)

    # Format the datetime in the desired format
    desired_format = iso8601_datetime.strftime("%B %d, %Y %H:%M:%S UTC")

    return desired_format

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
        
        messages = question['question']['response']['message']
        print("Comments: ")
        for message in messages:
            content = message['content']
            date = format_iso8601(message['createAt'])
            name = message['senderFirstName'] + ", " + message['senderLastName']
            print(f"{date} {name}: {content}")
        
        print()
