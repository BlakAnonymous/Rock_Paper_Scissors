from random import randint
#create a list of playable options
t = ["Rock", "Paper", "Scissors"]
#assign a random play to the computer
computer = t[randint(0,2)]
#set player to false]
player = False

while player == False:
#set player to true
      player = input("Rock, Paper, Scissors?")
      if player == computer:
          print("Tie!")
      elif player == "Rock":
          if computer == "Paper":
              print("You loose!", computer, "covers", player)   
          else:
              print("You win!", player, "smashes", computer)         
      elif player == "Paper":
          if computer == "Scissors":
              print("You loose!", computer, "cuts", player)
          else:
              print("You win!", player, "covers", computer)    
      elif player == "Scissors":
          if computer == "Rock":
              print("You loose!", computer, "smashes", player) 
          else:
              print("You win!", player, "cuts", computer) 
      else: 
        print("That is not a valid play, check spelling.")
        #player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[randint(0,2)]      
              
                             