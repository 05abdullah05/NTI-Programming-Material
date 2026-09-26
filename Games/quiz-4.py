#This code is a back up if the other game doesnt work

import random
Game_over = False
def start_game():
   global start
   start = str(input('Do you want to start the game? (yes/no):'))
   if start == 'yes':
      print("Welcome to quiz of Life!")
      print('Game started!')
      print('') #Space between lines


def starting_point():
   global Game_over
   #This function checks if you have chosed yes in the previous question.
   if start == 'no':
       print('Game over :(')
       Game_over=True
   else:
       print("The game of sports has began!") 


def continue_game():
    questions = [
    ("Where are the FIFA footballs made? ", "Pakistan"), 
    ("Which boxer fought against Muhammad Ali and won? ", "Joe Frazier"),
    ("How long is a marathon?", "42.195km"),
    ("The Olympics are held every how many years?", "4 years"),
    ("In motor racing, what color is the flag they wave to indicate the winner?", "Checkered flag"),
    ("What color are the goalposts in football?","Yellow"),
    ("What do the rings in the Olympics represent?","Continents")]
    random.shuffle(questions)
    points = 0
    i = 0
    streak = 0
    pointStreak = 0

    while i < len(questions):          #It checks when i is smaller than the list
      s = input(questions[i][0] + " ") #This asks for an answer from the user # i is the index in the questions list meaing what questions to come. 0 is the index of one of the elements in questions list so the 0th index of the one of the questions.
      if s == questions[i][1]:         #this compares the answer with the facit and compare it
        points += 1+pointStreak
        streak +=1
        print("Correct! You have", points,"points!")
      else:
        streak = 0
        points -= 1
        print("Wrong! You have ", points,"points!")
        questions.append(questions[i])
      if streak == 3:
        pointStreak +=2
        print("NICE YOURE ON A STREAK ;)")
      i += 1
    
    print("You got total", points, "points!")
    u = input("Would you like to give another chance? (yes/no): ")
    if u == "yes":
      print("Try to be quicker this round!")
      continue_game()
    else:
      Game_over = True


start_game()
continue_game()
starting_point()

#https://parade.com/1182514/marynliles/sports-trivia/ LINK TO QUESTIONS

    
        
