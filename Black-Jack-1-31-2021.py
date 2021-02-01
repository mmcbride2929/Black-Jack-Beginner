import random

def is_blackjack(player_win, computer_win):
    global win
    if player_win == 21:
        win = True
          
    elif computer_win == 21:
        win = True    
        
def is_bust(play_hand, comp_hand):
    global win
    if sum(play_hand) > 21:
        if 11 in play_hand:
            play_hand.remove(11), play_hand.append(1)
            player_score = sum(player_hand)
          #  print("potato")
            return player_score
            if sum(play_hand) > 21 :
               win = True
               return win    
        elif sum(play_hand) > 21:
            win = True    
            return win
    if sum(computer_hand) > 21:
        if 11 in comp_hand:
            comp_hand.remove(11), comp_hand.append(1)
            computer_score = sum(computer_hand)
            return computer_score
            if sum(play_hand) > 21:
                win = True
                return win
        elif sum(comp_hand) > 21:
            win = True
            return win   

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = random.choices(cards, k=2)
computer_hand = random.choices(cards, k=2)

player_score = sum(player_hand)
computer_score = sum(computer_hand)
win = False
player_draw = True

print(f"Your hand: {player_hand}, your score: {player_score}")
print(f"Computer's first card: {computer_hand[0]}")

while win == False:

    while player_draw == True:

        is_bust(player_hand, computer_hand)
        if win == True:
            break
        draw_card = input("Type 'y' to draw another card & type 'n' to pass: ").lower()

        if draw_card == "y":
            player_hand.append(random.choice(cards))
            is_bust(player_hand, computer_hand)
            player_score = sum(player_hand)
            if win == True:
                player_draw = False
            print(f"Your hand: {player_hand}, your score: {player_score}")
            print(f"Computer's first card: {computer_hand[0]}")
        else:
            player_draw = False
            
    
    is_bust(player_hand, computer_hand)
    if win == True:
                player_draw = False
    while computer_score < 21 or win == False:
        if computer_score < 16:           
            computer_hand.append(random.choice(cards))
            #computer_score = sum(computer_hand)
            is_bust(player_hand, computer_hand)
            computer_score = sum(computer_hand)
           # print("crash0")
            #print(computer_hand)
            if win == True:
              #  print("crash1")
                break
                
        elif computer_score <= 21 and computer_score <= player_score:
            computer_hand.append(random.choice(cards))
            is_bust(player_hand, computer_hand)
            computer_score = sum(computer_hand)
            #print("crashB")
            if win == True:
              #  print("crashB")
                break
                
        elif computer_score > player_score and computer_score <= 21:
          # print("test")
            win = True
            break
        else:
          # print(computer_hand)
         #   print(computer_score)
         #   print(player_hand)
          #  print("else")
            break
                                                     
print(f"Your final hand {player_hand} your final score: {player_score} ")
print(f"Computer hand {computer_hand} Computer final score: {computer_score}")

#is_blackjack(player_score, computer_score)
#is_bust(player_hand, computer_hand)

if player_score == 21 or computer_score == 21:
    if player_score == 21:
        print("Blackjack! You win!")
    elif computer_score == 21:
        print("Blackjack! You lose!")

if player_score > 21 or computer_score > 21:
    if player_score > 21:
       print("You went over. You lose ")        
    elif computer_score > 21:
        print("Opponent went over. You win ")    
           
if player_score <= 21 and computer_score <= 21:
    if player_score > computer_score:       
        print("You win ")
    elif computer_score > player_score:
        print("You lose ")
    elif computer_score == player_score:
        print("Draw")

