# Quiz Game

questions = ("1. How many elements are in the periodic table?:",
             "2. Which animal lays the largest eggs?: ",
             "3. What is the most abundant gas in Earth's atmosphere?: ",
             "4. How many bones are in the human body?: ",
             "5. Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 118", "C. 120", "D. 112"),
           ("A. Elephant", "B. Whale", "C. Ostrich", "D. Crocodile"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Argon"),
           ("A. 206", "B. 208", "C. 210", "D. 212"),
           ("A. Mercury", "B. Venus", "C. Mars", "D. Jupiter"))

answers = ("B", "C", "B", "A", "B")

guesses = []

score = 0

ques_num = 0

for question in questions:
    print("-------------------")
    print(question)
    for option in options[ques_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    
    if guess == answers[ques_num]:
        score += 1
        print(f"{answers[ques_num]} is the correct Answer")
    
    else:
        print("Incorrect Answer")
        print(f"{answers[ques_num]} is the correct answer.")
    
    ques_num += 1

print("-------------------")
print("-     Results     -")
print("-------------------")

print("answers: ", end = " ")

for answer in answers:
    print(answer, end = " ")
print()   

print("guesses: ", end = " ")
for guess in guesses:
    print(guess, end = " ")
print()   

score = (score / len(questions) * 100)
print(f"Your Score is: {score}")