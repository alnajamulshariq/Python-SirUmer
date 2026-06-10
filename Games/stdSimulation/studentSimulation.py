print("Wellcome to Student Simulation Game")

choice = int(input("""
        Select an option you want to perform?
        1- Study
        2- Exercise
        3- Rest
        """))

match choice:
    case 1:
        print("you select the option for Studying .....")
        study_choice = int(input("""
        Select an option you want to perform?
        1- Study alone
        2- Group Study
        """))
        if study_choice == 1:
            print("study alone \nkeep working hard ")
        elif study_choice == 2:
            print("Group Study \nbest of Luck ")
        else:
            print("Try Again...")
    case 2:
        print("you select the option for Exercise .....")
        exercise_choice = int(input("""
        Select an option you want to perform?
        1- Exercise at home
        2- Exercise at gym
        """))
        if exercise_choice == 1:
            print("Exercise at home \nkeep up the good work!")
        elif exercise_choice == 2:
            print("Exercise at gym \nGreat job staying fit!")
        else:
            print("Try Again...")
    case 3:
        print("you select the option for Rest .....")
        rest_choice = int(input("""
        Select an option you want to perform?
        1- Sleep
        2- Watch TV
        """))
        if rest_choice == 1:
            print("Sleep \nYou need rest to perform well!")
        elif rest_choice == 2:
            print("Watch TV \nRelax and enjoy!")
        else:
            print("Try Again...")