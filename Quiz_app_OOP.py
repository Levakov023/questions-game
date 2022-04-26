class Quest:
    def __init__(self, texta, answerb):
        self.text = texta
        self.answer = answerb
    # Question where you input text and the answer or append it from a dict using key and value

    def display(self):
        print(f"Text :{self.text}")
        print(f"Answer : {self.answer}")
    # Shows you both text and the answer to the question.


class Play:
    def __init__(self, q_list):
        self.question_number = 0
        self.list = q_list
        self.playing = True
        self.correct = 0
    # q_list is the list of all the question classes in a list.

    def endquiz(self):
        return self.question_number < len(self.list) and self.playing
    # checks if player guessed a question incorrectly or has reached the end of the quiz.

    def end(self):
        if self.correct == len(self.list):
            print(f"Congratulations, you've won! You've answered all {len(self.list)} questions correctly !")
        else:
            print(f"Game over, you lost! , you've got {self.correct} out of {len(self.list)} questions right!")
    # checks if the player got all the questions right else it prints out "youve lost " message

    def nextquestion(self):
        # generates the question and asks user for input of "True " or "False"
        current_question = self.list[self.question_number]
        # displays current question based on the self.question_number (begins at 0 by default)
        self.question_number += 1
        # moves to the next question
        if input(f" Question {self.question_number} : "
                 f"{current_question.text} (True)/(False)\n").capitalize() == current_question.answer:
            print("Correct")
            self.correct += 1
            # marks all correct answers for later
        else:
            self.playing = False
            # if incorrect, playing = False will return "False" at endquiz(self) thus ending the game


question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
             " you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament,"
             " you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Quest(text, answer)
    bank.append(new_question)
    # To display all the answers write bank[question index].display()

print(bank[1].display())


quiz = Play(bank)

while quiz.endquiz():
    quiz.nextquestion()
quiz.end()

print(bank[7].display())
