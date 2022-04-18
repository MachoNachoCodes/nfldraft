# Football game, still thinking on what specifically to do on this project but it will have to do with football
# I will use scratch if i want a visual for this project, as it is easier to do visuals with the things i want on scratch
# It's gonna be a quiz or a football game but i am still brainstorming which one
from random import *
from time import *

def freeAgency():
 money = 1200
 picks = 3
 print("Pick your defensive player, each player is 400 dollars, your team has a budget of $1200 dollars")
 sleep(5)
 print("1. OLB 2x Super Bowl champion Von Miller")
 print("2. Cardinals superpower OLB Chandler Jones")
 print("3. Seattle ILB Bobby Wagner")
 print("4. Jaguars ILB Myles Jack")
 print("5. Texans Safety Justin Reid")
 print("6. KC Chiefs Cornerback Charvarius Ward")
 while True:
   faList = ["Von Miller", "Chandler Jones", "Bobby Wagner", "Myles Jack", "Justin Reid", "Charvarius Ward"]
   userInput = input()
   if userInput in faList:
    print("You chose")
    print(userInput)
    money = money - 400
    print("You now have " + str(money) + " dollars left")
    picks = picks - 1
    print(str(picks) + " picks left")
    playersDrafted.append(userInput)
   if userInput not in faList:
     print("Pick a valid free agent")
   if picks == 0:
     print("You have picked all of your free agents!")
     break


teamList = ["Jacksonville Jaguars", "Detroit Lions", "Cleveland Browns", "Carolina Panthers", "New York Giants", "New York Jets", "Washington Commanders", "Miami Dolphins"]
playersDrafted = []
print("Welcome to the NFL 2022 Draft, your team is the " + choice(teamList))
sleep(3)
print("Let's start with quarterbacks, who would you like to pick?")
print("Your options are Kenny Pickett out of Pitt or Malik Willis out of Liberty")
while True:
   qbList = ["Kenny Pickett", "Malik Willis"]
   userInput = input()
   if userInput == "Kenny Pickett":
    playersDrafted.append("Kenny Pickett")
    qbList.pop(0)
    print("You chose Kenny! He's a strong armed quarterback who can operate in the pocket well.")
    break
   if userInput == "Malik Willis":
    playersDrafted.append("Malik Willis")
    qbList.pop(1)
    print("You chose Malik! He is a fast and efficient qb who can break through defenses easily")
    break
   if userInput != qbList:
     print("Please choose a quarterback")
print("Your players so far are")
print(playersDrafted)
print("Good QB choice! Next category is wide receivers")
sleep(5)
print("Wide recievers make up one of the biggest roles to fill for a team, choose wisely. This will decide your teams success")
while True:
 print("Your options are Garrett Wilson out of Ohio State, Drake London out of USC and Jameson Williams out of Alabama")
 userInput = input()
 wrList = ["Garrett Wilson", "Drake London", "Jameson Williams"]
 if userInput == "Garrett Wilson":
  print("#1 Wide Reciever, good choice. Ohio State produces the best wide receivers")
  playersDrafted.append("Garrett Wilson")
  wrList.pop(0)
  break
 if userInput == "Drake London":
  print("#2 WR in the draft and out of USC, very talented, good route runner. Lets see if he brings this college talent to the NFL")
  playersDrafted.append("Drake London")
  wrList.pop(1)
  break
 if userInput == "Jameson Williams":
  print("#3 in the draft and a great wide reciever, Alabama is a great program and he will bring success to your team")
  playersDrafted.append("Jameson Williams")
  wrList.pop(2)
  break
 if userInput != wrList:
  print("Pick a Wide Receiver")
sleep(3)
print("Your players so far are")
print(playersDrafted)
sleep(1)
print("Now it is time for defense, this year, the NFL is only letting teams pick from free agency. Pick 3 free agents for your defense.")
freeAgency()
sleep(10)
print("Thank you for participating in the 2022 NFL Draft, here are your draft selections and your new defensive free agent pickups!")
print(playersDrafted)
  



    
     
    
  
  
  
  
  


  
  
    
    
  
    
  
   
   
    
   
   
   
   
   
     
    