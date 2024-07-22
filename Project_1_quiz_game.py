#Python project 1
#quiz game
#below code can also be written using classes but here is the simpler version of it using loops

print("                      WELCOME TO QUIZ                ")
print('\n')

# Define the questions, options, and correct answers via list and dictinary
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Rome'],
        'correct_answer': 'Paris'
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'options': ['Earth', 'Saturn', 'Jupiter', 'Uranus'],
        'correct_answer': 'Jupiter'
    },
    {
        'question': 'What is the smallest country in the world?',
        'options': ['Vatican City', 'Monaco', 'Nauru', 'Tuvalu'],
        'correct_answer': 'Vatican City'
    }
]

# Initialize the score
score = 0

# Run the quiz via loop
for question in questions:
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    while True:
        try:
            user_answer = input("Enter the number of your answer: ")
            user_answer = question['options'][int(user_answer) - 1]
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number.")
    if user_answer == question['correct_answer']:
        print("Correct!")
        print('\n')
        score += 1
    else:
        print(f"Incorrect. The correct answer is {question['correct_answer']}")
        print('\n')

# Display the final score with remarks
if score>=2:
    print(f"Well done! \nYour final score is {score} out of {len(questions)}")
else:
    print(f"Well tried! \nYour final score is {score} out of {len(questions)}")
