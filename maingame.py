# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

def draw():
  return randint(1,13)

def card_processor(card_rank):
  drew_prefix=''
  card_name=''
  if card_rank == 1:
    card_name = "Ace"
  elif card_rank == 11:
    card_name = "Jack"
  elif card_rank == 12:
    card_name = "Queen"
  elif card_rank == 13:
    card_name = "King"
  else:
    card_name = str(card_rank)

  if card_rank == 1 or card_rank == 8:
    drew_prefix = 'Drew an '
  else:
    drew_prefix = 'Drew a '
  print(drew_prefix+card_name)

def card_value(card_rank):
  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    return 10
  elif card_rank == 1:
    return 11
  else:
    return card_rank  

def process_hand(user_hand):
  if user_hand==21:
    print("Final hand: 21.")
    print("BLACKJACK!")
    return True
  elif user_hand>21:
    print("Final hand:",str(user_hand)+".")
    print("BUST.")
    return True
  else:
    return False

def check_if_final_hand(dealer_hand):
  if dealer_hand==21:
    print("Final hand: 21.")
    print("BLACKJACK!")
  elif dealer_hand>21:
    print("Final hand:",str(dealer_hand)+".")
    print("BUST.")
  elif dealer_hand>=17 and dealer_hand<21:
    print("Final hand:",str(dealer_hand)+".")
  elif dealer_hand<17:
    print("Dealer has",str(dealer_hand)+".")


print("-----------")
print("YOUR TURN")
print("-----------")
card_1=draw()
card_2=draw()
card_processor(card_1)
card_processor(card_2)
user_hand=card_value(card_1)+card_value(card_2)
if user_hand >=21:
  process_hand(user_hand)
else:
  while process_hand(user_hand)==False:
    user_input=input("You have "+str(user_hand)+"."+" Hit (y/n)? ")
    if user_input == "n":
      print("Final hand:",str(user_hand)+".")
      break
    elif user_input == "y":
      card=draw()
      user_hand = user_hand + card_value(card)
      card_processor(card)
    else:
      print("Sorry I didn't get that.")

print("-----------")
print("DEALER TURN")
print("-----------")
card_1=draw()
card_2=draw()
card_processor(card_1)
card_processor(card_2)
dealer_hand=card_value(card_1)+card_value(card_2)
check_if_final_hand(dealer_hand)
card=0
while dealer_hand<17:
  card=draw()
  dealer_hand = dealer_hand + card_value(card)
  card_processor(card)
  check_if_final_hand(dealer_hand)

print("-----------")
print("GAME RESULT")
print("-----------")
if (user_hand<dealer_hand and dealer_hand<=21) or user_hand>21:
  print("Dealer wins!")
elif (user_hand>dealer_hand and user_hand<=21) or (dealer_hand>21 and user_hand<=21):
  print("You win!")
elif user_hand==dealer_hand and user_hand<=21:
  print("Push.")

