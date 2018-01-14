#Andrew Schultz's Blackjack

import random
def main():

  #Introduction
  print("Hi welcome to BlackJack!")
  print("Here are your cards.")

  #calling the first two cards and printing them
  card1 = first_cards()
  card2 = first_cards()
  print("")
  print(card1)
  while card2 == card1:
    card2 = first_cards()
  print(card2)
  print("")

  #Calculating total score for the two cards
  score_atm = calculate_score(card1, card2)
  print("Your current score is", score_atm )
  if score_atm == 21:
    print("BlackJack you win!")

  #House's cards
  print("")
  house_one = dealers_card()
  print("The house is showing", house_one, "points with their face-up card.")
  print("What could their face-down card be?")
  print("")
  house_two = dealers_card()
  house_hand = house_one + house_two

  #Asking if they want to hit
  hit_var = input("Would you like to hit? (Y/N) ")
  print("")

  #Validation loop
  if hit_var.upper() != "Y" and hit_var.upper() != "N":
    hit_var = input("Try again. Valid answers are Y and N. ")

  #If they choose not to hit at all
  if hit_var.upper() != "Y":
    new_score = score_atm
  #Choosing to hit
  while hit_var.upper() == "Y":
    new_score = hit(score_atm)

    #Breaking
    if new_score == 1:
      print("Looks like you broke.")
      print("")
      hit_var = "N"

    #If they get 21 stop the loop
    elif new_score == 21:
      hit_var = "N"

    #If they hit and are less than 21
    else:
      score_atm = new_score
      print("")
      hit_var = input("Would you like to hit again? (Y/N) ")
      print("")

  #Dealers hitting loop
  while house_hand < 15:
    print("The dealer hits.")
    house_x = dealers_card()

    #For ace's on the hit
    if house_x == 11:
      house_x = 1
    house_hand = house_hand + house_x

  #Deciding and printing who won
  if house_hand > 21 and new_score != 1:
    print("The house broke.")
    print("YOU WIN!")
  elif new_score == 1 and house_hand > 21:
    print("The house broke also.")
    print("Draw.")
  elif house_hand < 22 and new_score == 1:
    print("The house had ",house_hand)
    print("House wins.")
  elif house_hand > new_score:
    print("The house had ", house_hand)
    print("House wins.")
  elif house_hand == new_score:
    print("The house had ", house_hand)
    print('Draw.')
  else:
    print("The house had ", house_hand)
    print("YOU WIN!")
  print("Thanks for playing. Type main() to play again!") 

#Getting the cards 
def first_cards():
  cardnum = random.randint(1,13)
  suitnum = random.randint(1,4)

  card = card_processer(cardnum, suitnum)
  return card

#Interpreting the card numbers into names
def card_processer(cardnum, suitnum):
  card = ""
  suit = ""

  #Interpreting "word" cards 
  if cardnum == 1:
      card = "Ace"
  elif cardnum == 11:
      card = "Jack"
  elif cardnum == 12:
      card = "Queen"
  elif cardnum == 13:
      card = "King"
  elif cardnum <= 10:
      card = cardnum

  #Interpreting numbers into suit names
  if suitnum == 1:
      suit = "Spades"
  elif suitnum == 2:
       suit = "Hearts"
  elif suitnum == 3:
       suit = "Diamonds"
  elif suitnum == 4:
       suit = "Clubs"
  cardname = str(card) + " of " + str(suit)
  return cardname

#interpreting the above names into the correct values
def calculate_score(card1, card2):
  value1 = 0
  value2 = 0

  #This is for kings queens ace's and jacks
  if card1[0] == "K" or card1[0] == "Q" or card1[0] == "J" or card1[0] == "1":
    value1 = 10
  elif card1[0] == "A":
    pick = int(input("Would you like the Ace to equal 1 or 11? "))
    while pick != 1 and pick != 11:
      pick = int(input("Please try again. The choices are 1 or 11."))
    if pick == 1:
      value1 = 1
    elif pick ==11:
      value1 = 11

  #For number cards
  else:
    value1 = int(card1[0])

  #Same deal here  
  if card2[0] == "K" or card2[0] == "Q" or card2[0] == "J" or card2[0] == "1":
    value2 = 10
  elif card2[0] == "A":
    pick = int(input("Would you like the Ace to equal 1 or 11? "))
    while pick != 1 and pick != 11:
      pick = int(input("Please try again. The choices are 1 or 11."))
    if pick == 1:
      value2 = 1
    elif pick == 11:
      value2 = 11

  #Number cards
  else:
    value2 = int(card2[0])

  #Total of two cards
  total = value1 + value2
  return total
  
#Hit function for user
def hit(score):

  #Getting a new card and interpreting its value
  new_score = 0
  cardnum = random.randint(1,13)
  if cardnum == 10 or cardnum == 11 or cardnum == 12 or cardnum == 13:
    new_score = score + 10
  elif cardnum == 1:
    pick = int(input("Would you like the Ace to equal 1 or 11? "))

    #Validation loop for ace's
    while pick != 1 and pick != 11:
      pick = int(input("Please try again. The choices are 1 or 11. "))
    if pick == 1:
      new_score = score + 1
    elif pick == 11:
      new_score = score + 11

  #Getting the score
  else:
    new_score = score + cardnum

  #Numbers back into cards
  if cardnum == 11:
    cardnum = "Jack"
  elif cardnum == 12:
    cardnum = "Queen"
  elif cardnum == 13:
    cardnum = "King"
  elif cardnum == 1:
    cardnum = "Ace"

  #Providing new score
  if new_score < 22:
    print("Your next card was a(n)", cardnum)
    print("Your new score is", new_score)
    return new_score
  #This is for if they broke
  else:
    print("Your next card was ", cardnum)
    return 1

#Getting the dealers cards
def dealers_card():
  card = random.randint(1,13)
  if card == 1:
    value = 11
  elif card == 11 or card == 12 or card ==13:
    value = 10
  else:
    value = card
  return value

main()
