def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print ("*"*20)
        print(key)
        for i in options[question_num - 1]:
            print (i)

        while True:
            guess = input("Enter (A, B, C, D): ")
            guess = guess.upper()
            if guess != "A" and guess != "B" and guess != "C" and guess != "D":
                print ("Unvaible option")
            else:
                guesses.append(guess) 
            correct_guesses += check_answer(questions.get(key), guess)
             
            question_num += 1
             

    display_score(correct_guesses, guesses)
# -----------------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print ("CORRECT!!")
        return 1
    else:
        print ("WRONG!!")
        return 0

# -----------------------------
def display_score(correct_guesses, guesses):
    print ("*"*20)
    print ("RESULTS")
    print ("*"*20)
    print ("Answers: ", end=" ")
    for i in questions:
        print (questions.get(i), end=" ")
    print()

    print ("Guesses: ", end=" ")
    for i in guesses:
        print (i, end=" ")
    print ()

    score = int((correct_guesses/len(questions)) * 100)
    print ("Your score is:"+str(score)+"%")
    
    
# ------------------------------
def play_again():
    
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

# ------------------------------

questions = {
   
    "With witch item Pearl killed Misty?" : "C",
    "When Scarface was released?" : "A",
    "Name the actor that played Billy Lo in Game of Death" : "D",
    "Name the song that Pearl dances in X" : "A",
    "Who is the director of The Godfather?": "B",
    "Who is the author of the book that inspired American Pyscho?" : "C"

}  

options = [["A. Knife", "B. Hammer", "C. Axe", "D. Pitchfork"],
          ["A. 1983", "B. 1989", "C. 1979", "D. 1987"],
          ["A. Jackie Chan", "B. Tony Leung Chiu Wai", "C. Leslie Cheung", "D. Bruce Lee"],
          ["A. Oui Oui Marie", "B. I Wanna Be Loved by You", "C. Perhaps Perhaps Perhaps", "D. These Boots Are Made For Walkin"],
          ["A. James Cameron", "B.Francis Ford Coppola", "C. Martin Scorcese", "D. Quentin Tarantino"],
          ["A. Chuck Palanihuk", "B. Mario Puzo", "C. Bret Easton Ellis", "D. Franz Kafka"]]


new_game()

while play_again():
    new_game()

print ("Byeeeeeeeeeee!")

