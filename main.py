loginInfoDictionary = {
    "username": "PGR107",
    "password": "python"
}

questions = [
    {
        "question": "What is the capital of Norway?",
        "a": "Bergen",
        "b": "Oslo",
        "c": "Stavanger",
        "d": "Trondheim",
        "correct": "b"
    },
    {
        "question": "What is the currency of Norway?",
        "a": "Euro",
        "b": "Pound",
        "c": "Krone",
        "d": "Deutch Mark",
        "correct": "c"
    },
    {
        "question": "What is the largest city in Norway?",
        "a": "Oslo",
        "b": "Stavanger",
        "c": "Bergen",
        "d": "Trondheim",
        "correct": "a"
    },
    {
        "question": "When is Constitution Day (the national day) of Norway?",
        "a": "27th of May",
        "b": "17th of May",
        "c": "17th of April",
        "d": "27th of April",
        "correct": "b"
    },
    {
        "question": "What color is the background of the Norwegian flag?",
        "a": "Red",
        "b": "White",
        "c": "Blue",
        "d": "Yellow",
        "correct": "a"
    },
    {
        "question": "How many countries does Norway border?",
        "a": "1",
        "b": "2",
        "c": "3",
        "d": "4",
        "correct": "c"
    },
    {
        "question": "What is the name of the university in Trondheim?",
        "a": "UiS",
        "b": "UiO",
        "c": "NMBU",
        "d": "NTNU",
        "correct": "d"
    },
    {
        "question": "How long is the border between Norway and Russia (in km)?",
        "a": "96",
        "b": "196",
        "c": "296",
        "d": "396",
        "correct": "b"
    },
    {
        "question": "Where in Norway is Stavanger?",
        "a": "North",
        "b": "South",
        "c": "South-west",
        "d": "South-east",
        "correct": "c"
    },
    {
        "question": "From which Norwegian city did the world’s famous composer Edvard Grieg come?",
        "a": "Oslo",
        "b": "Bergen",
        "c": "Stavanger",
        "d": "Tromsø",
        "correct": "b"
    }
]

def login_info(gUsername, gPassword):
    return gUsername == loginInfoDictionary.get("username") and gPassword == loginInfoDictionary.get("password")

# Checking that the input is valid and if the answer is correct
def check_answer(question, answer):
    if answer in ["a", "b", "c", "d"]:
        return question["correct"] == answer
    else:
        return False

def quiz():
    print("Welcome to the quiz!")
    
    # Login
    while True:
        username = input("Username: ")
        password = input("Password: ")
        if login_info(username, password):
            print("You are logged in!")
            break
        else:
            print("Wrong username or password. Try again.\n")

    # Starting the quiz
    print("Let's start the quiz!\n")
    score = 0
    inncorectAnswersList = []
    # Going through the questions  
    for q in questions:
        while True:    
            print(q["question"])
            print(f"a) {q['a']}")
            print(f"b) {q['b']}")
            print(f"c) {q['c']}")
            print(f"d) {q['d']}")
            
            answer = input("Your answer: ").strip().lower()
            
            if check_answer(q, answer):
                print("Correct!\n")
                score += 1
                break
            elif answer in ["a", "b", "c", "d"]:
                print(f"Wrong! The correct answer was {q[q['correct']]}\n")
                # Save the questions that were incorect
                inncorectAnswersList.append({"wrongQuestion": q["question"], "wrongAnswer": q[q['correct']]})
                break
            else:
                print("Invalid answer! Please choose a, b, c or d.")
            

    print(f"Quiz finished! Your final score: {score}/{len(questions)}")
    print("Incorrect answers:")
    for i in inncorectAnswersList:
        print(f"{i['wrongQuestion']}:\n {i['wrongAnswer']}\n")
quiz()


