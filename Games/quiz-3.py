import random  

Game_over = False   #This variable is used when the game is ended and it will turn true then.
def start_game(): #This funtion is the menu for game
   global start
   start = str(input('Do you want to start the game? (yes/no):'))
   if start == 'yes':
      print('')
      print("Welcome to quiz of Life!")
      print('Game started!')
      print("The answers are in lower case, don't forget the space if the answer is long!")
      print("Good Luck")
      nivå1_game()
      print('') #Space between lines
   elif start == 'no':
      print('Game over :(')
      Game_over=True

#This function is the for the 1st level
def nivå1_game():
    print("")
    print("1st level is about sports!")
    questions = [
    ("Where are the FIFA footballs made? ", "pakistan"), 
    ("Which country won the most FIFA WC? ", "brazil"),
    ("What basketball team has the longest winning streak?", "la lakers"),
    ("The Olympics are held every how many years?", "4"),
    ("Who is the youngest ever world heavyweight boxing champion?","mike tyson")]
    random.shuffle(questions)#This is used to randomize the questions list
    points = 0       #This variable is used to count points 
    i = 0            #This variable is used for indexing variable
    streak = 0       #This variable is used to now how many questions you answered correct 
    pointStreak = 0  #This variable will give you 3 points if variable streak is true

    while i < len(questions):                  #It checks when i is smaller than the list
      s = input(questions[i][0] + " ").lower() #This asks for an answer from the user
      if s == questions[i][1]:                 #this compares the answer with the facit and compare it
        points += 1+pointStreak
        # points = points+1+pointsstreak
        streak +=1
        print("Correct! You have", points,"points!")
      else:                           #This checks if you have wrong answer
        streak = 0
        points -= 1               
        print("Wrong! You have ", points,"points!")
        questions.append(questions[i]) #This will save questions which you got wrong on and those questions will appear again after every question has been asked from the list
      if streak == 2:                  #This if is checking if you answer questions in a row and if so then it gives you 2 extra points.
        pointStreak +=2
        print("NICE YOURE ON A STREAK ;)")
      i += 1

    print("You got total", points, "points!")
    print("")
    u = input("Would you like to do the next level? (yes/no): ")
    if u == "yes":
      print("Try to be quicker this round!")
      nivå2_game() #This calls for the 2 nd level to begin
    elif u == "no":
      Game_over = True
      print("Have a nice day, welcome back!")

#This function is the for the 2nd level
def nivå2_game():
    print("2nd level is about history!")
    print("")
    questions = [
    ("Who was the first person to land on the moon? ", "neil armstrong"), 
    ("What was the code name for the German invasion of the Soviet Union during World War II? ", "operation barbarossa"),
    ("Who was the first Emperor of Rome?", "augustus"),
    ("What year was Facebook created?", "2004"),
    ("Who won the 2008 U.S. Presidential election?","barack obama")]
    random.shuffle(questions)
    points = 0       #This variable is used to count points 
    i = 0            #This variable is used for indexing variable
    streak = 0       #This variable is used to now how many questions you answered correct 
    pointStreak = 0  #This variable will give you 3 points if variable streak is true

    while i < len(questions):                  #It checks when i is smaller than the length of the list
      s = input(questions[i][0] + " ").lower() #This asks for an answer from the user
      if s == questions[i][1]:                 #this compares the answer with the facit and compare it
        points += 1
        print("Correct! You have", points,"points!")
      else:
        streak = 0
        points -= 1
        print("Wrong! You have ", points,"points!")
        questions.append(questions[i]) #This will save questions which you got wrong on and those questions will appear again after every question has been asked from the list
      if streak == 2:                  #This if is checking if you answer questions in a row and if so then it gives you 2 extra points.
        pointStreak +=2
        print("NICE YOURE ON A STREAK ;)")
      i += 1

    print("You got total", points, "points!")
    Game_over = True
    print("")
    u = input("Would you like to do the next level? (yes/no): ")
    if u == "yes":
      print("Try to be quicker this round!")
      nivå3_game()
    else:
      Game_over = True
    
#This function is the for the 3rd level
def nivå3_game():
    print("3rd level is about contries") 
    print("")
    questions = [
    ("What are the names of the five oceans of the world? ", "atlantic pacific indian arctic antarctic"), 
    ("How many States does the United States consist of?", "50"),
    ("What planet is closest to Earth?", "venus"),
    ("What is the name of the tallest mountain in the world?", "mount everest"),
    (" What is the name of the smallest country in the world?","vatican city")]
    random.shuffle(questions)
    points = 0       #This variable is used to count points 
    i = 0            #This variable is used for indexing variable
    streak = 0       #This variable is used to now how many questions you answered correct 
    pointStreak = 0  #This variable will give you 3 points if variable streak is true
    
    while i < len(questions):                  #It checks when i is smaller than the list
      s = input(questions[i][0] + " ").lower() #This asks for an answer from the user
      if s == questions[i][1]:                 #This compares the answer with the facit and compare it
        points += 1
        print("Correct! You have", points,"points!")
      else:
        streak = 0
        points -= 1
        print("Wrong! You have ", points,"points!")
        questions.append(questions[i]) #This will save questions which you got wrong on and those questions will appear again after every question has been asked from the list
      if streak == 2:                  #This if is checking if you answer questions in a row and if so then it gives you 2 extra points.
        pointStreak +=2
        print("NICE YOURE ON A STREAK ;)")
      i += 1

    print("You got total", points, "points!")
    Game_over = True
    #The lines of code below will ask the user if they are intrested in doing any of the levels above again or not.
    #If yes then they also have the option to chose which level they would like to try again
    u = input("Would you like to do any of the levels again? (yes/no): ")
    if u == "yes":
      z= input("Which level? (nivå1/nivå2/nivå3)")
      if z=="nivå1":
        print("Good Luck this time")
        nivå1_game()
      elif z == "nivå2":
        nivå2_game()
      elif z == "nivå3":
        print("You are not going to give up easily")
        nivå3_game()
      else:
        print("You are welcom back again")
        Game_over = True
        
start_game()