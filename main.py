from deck import *


# Changes is from a string to an integer
def change_rank(card):
        if card.rank in ["Jack", "Queen", "King"]:
            return 10
        elif card.rank == "Ace":
            return 11
        else:
            return int(card.rank)

# Adds the cards 
def add_cards(cards):
    totals = []
    total = 0
    num_of_aces = 0
    for card in cards:
        card_value = change_rank(card)
        if card.rank == "Ace":
            num_of_aces += 1
        total += card_value
    totals.append(total)
    # Adjust for Aces
    for i in range (num_of_aces):
        total -= 10
        totals.append(total)
    return totals





def play_game(deck=None):
    # Seeing if you put a test case in otherwise do a normal deck
    if deck == None:
        deckOfCards = DeckOfCards()
        deckOfCards.shuffle_deck()
    else:
        deckOfCards = DeckOfCards(deck)

    # Deals cards
    card1 = deckOfCards.deal_card()
    card2 = deckOfCards.deal_card()
    house_card1 = deckOfCards.deal_card()
    house_card2 = deckOfCards.deal_card()

    # Gives the player a hand
    player_hand = [card1, card2]
    # Puts the hand into a readable string
    player_hand_string = f"a {card1} and a {card2}"
    # adds the cards in the hand
    player_scores = add_cards(player_hand)

    # Gives the house a hand
    house_hand = [house_card1, house_card2]
    # Puts the hand into a readable string
    house_hand_string = f"a {house_card1} and a {house_card2}"
    # adds the cards in the hand
    house_scores = add_cards(house_hand)

    print("\n")
    # Tells you what card the dealer is showing
    print(f"The dealer is showing a {house_card2}")
    print("\n")
    s = " or ".join(map(str, player_scores))
    # Prints what cards the player has and what it totals to
    print(f"You got {player_hand_string}, that is {s}.")
    keepgoing = True
    while keepgoing:
        print("\n")
        # Asks if they want to hit or stay
        hit_or_stay = input("Would you like to hit or stay?")
        if hit_or_stay.lower() == "hit" or hit_or_stay.lower() == "h":
            # If they hit then they do this
            # deal a card
            card3 = deckOfCards.deal_card()
            # add it to their hand
            player_hand.append(card3)
            # add all their cards
            player_scores = add_cards(player_hand)
            print("\n")
            s = " or ".join(map(str, player_scores))
            # Tells them what card was dealt and what the total is
            print(f"The card is {card3}, You now have {s}.")
            # check if all of the scores are over, and then say they busted
            bust_count = 0
            for score in player_scores:
                if score > 21:
                    bust_count += 1
                if bust_count == len(player_scores):
                    print("\n")
                    print(f"You got {card3}, that is {score}. You busted!")
                    keepgoing = False
        elif hit_or_stay.lower() == "stay" or hit_or_stay.lower() == "s":
            # If they said stay do this
            print("\n")
            s = " or ".join(map(str, house_scores))
            # Says what the house has and adds it together
            print(f"The house has {house_hand_string}, that is {s}.")
            # decide if dealer should hit or not
     
            kg = True
            while(kg):
                hbust_count = 0
                for hscore in house_scores:
                    if hscore < 17: # we should hit
                        print("\n")
                        card = deckOfCards.deal_card()
                        house_hand.append(card)
                        house_scores = add_cards(house_hand)
                        s = " or ".join(map(str, house_scores))
                        print(f"The dealer draws {card}. The dealers total is now {s}")
                        break
                    elif hscore > 21: # this score is busted
                        hbust_count += 1
                    else:
                        kg = False
                    if hbust_count == len(house_scores): 
                        # IF the dealer busts then it prints they win
                        print("\n")
                        print(f"The dealer busted with {hscore}. You win!")
                        keepgoing = False
                        kg = False
            hscore = 0
            # getting the highest non bust house number
            for housescore in house_scores:
                if housescore <= 21:
                    hscore = housescore
                    break
            score = 0
            # getting the highest non bust player number
            for pscore in player_scores:
                if pscore <= 21:
                    score = pscore
                    break
            if score > hscore:
                # If player scored higher print they won
                print("\n")
                print(f"You have {score} and the dealer has {hscore} Congratulations! You won!")
                keepgoing = False
            elif score < hscore:
                # If house scored higher they lost
                print("\n")
                print("Sorry you lost, the house got higher than you :(")
                keepgoing = False
            else:
                # If they have the same then print they tied
                print(f"It's a tie, you had {score}, and the house had {hscore}")
                keepgoing = False
        else:
            # They didn't type hit or stay
            print("\n")
            print("invalid option")

# Test case 1
# deck1 = DeckOfCards.stack_the_deck(
#     Card("Ace", Suit.Spades), 
#     Card("Ace",Suit.Diamonds), 
#     Card("Ace",Suit.Clubs), 
#     Card("Ace",Suit.Hearts),
#     Card("10",Suit.Hearts),
#     Card("9",Suit.Spades),
#     Card("10",Suit.Diamonds),
#     Card("5",Suit.Clubs),
#     Card("10",Suit.Clubs),
#     )
# play_game(deck1)

# Test case 2
# deck2 = DeckOfCards.stack_the_deck(
#     Card("Ace", Suit.Spades), 
#     Card("10",Suit.Diamonds), 
#     Card("Ace",Suit.Clubs), 
#     Card("10",Suit.Hearts),
#     Card("10",Suit.Hearts),
#     Card("6",Suit.Spades),
#     Card("Ace",Suit.Diamonds),
#     Card("5",Suit.Clubs),
#     Card("10",Suit.Clubs),
#     )
# play_game(deck2)


while True:
    play = input("Would you like to play BlackJack?")
    if play.lower() == "yes" or play.lower() == "y":
        # if they typed yes they want to play, play the game
        play_game()
        break
    elif play.lower() == "no" or play.lower() == "n":
        # If they don't want to play the game
        print("Okay, see you next time!")
        break
    else:
        # Didn't type yes or no
        print("invalid option")
