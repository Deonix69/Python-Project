def main():

    print("Which sentence would you like to choose?")
    print("There was a tiny (noun) who was feeling very (adjective).After (verb), they felt (adjective).")
    print("When the (adjective) (noun) decided to (verb). They wanted to (verb) even more!")
    print("The (adjective) (noun) attempted to get better at (verb) every day!")



    while True:
        choice = input("Sentence 1, 2, or 3?: ")
        if choice == "1":
            print("You chose sentence one! : 'There was a tiny (noun) who was feeling very (adjective).After (verb), they felt (adjective).' Now fill in the blanks!")
            noun1 = input("Noun: ")
            adjective1 = input("Adjective One: ")
            verb1 = input("Verb: ")
            adjective2 = input("Adjective Two: ")
            print(f"There was a tiny {noun1} who was feeling very {adjective1}. After {verb1}, they felt {adjective2}!")

        elif choice == "2":
            print("You chose sentence two! : 'When the (adjective) (noun) decided to (verb). They wanted to (verb) even more!' Now fill in the blanks!")
            adjective1 = input("Adjective: ")
            noun1 = input("Noun: ")
            verb1 = input("Verb One: ")
            print(f"When the {adjective1} {noun1} decided to {verb1}. They wanted to {verb1} more!")

        elif choice =="3":
            print("You chose sentence three! : 'The (adjective) (noun) attempted to get better at (verb) every day!' Now fill in the blanks!")
            adjective1 = input("Adjective: ")
            noun1 = input("Noun: ")
            verb1 = input("Verb: ")
            print(f"The {adjective1} {noun1} attempted to get better at {verb1} every day!")

        return choice

main()

