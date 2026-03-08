import random
import art

# now we define the functions. deal_card, calculate_score, and the main one, play_game

def deal_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)

def calculate_score(cards):
	# to score Blackjack
	if sum(cards)==21 and len(cards)==2:
		return 0

	# to switch Ace from 11 to become 1 when cards' total value is more than 21.
	if 11 in cards and sum(cards)>21:
		cards.remove(11)
		cards.append(1)

	return sum(cards)

# print art logo first. Deal the cards to user and computer.
def play_game():
	print(art.logo)

	is_game_over = False

	user_card = []
	dealer_card = []
	for _ in range(2):
		user_card.append(deal_card())
		dealer_card.append(deal_card())

	# USER'S TURN
	while not is_game_over:
		user_score=calculate_score(user_card)
		dealer_score=calculate_score(dealer_card)

		print(f"Your cards: {user_card}, current score: {user_score}")
	# Only show 1 card out of 2 on computer's hand
		print(f"Computer's first hand: {dealer_card[0]}")

	# To check whether user wins or loses
		if user_score==0:
			is_game_over= True
			print(f"You got Blackjack!")
		elif user_score>21:
			is_game_over=True
			print(f"You got bust! You lose!")
		elif dealer_score==0:
			is_game_over=True
			print(f"Dealer wins..")
		else:
			hit_or_stand=input(f"Do you want to draw another card? Y or N.: ").upper()
			if hit_or_stand=="Y":
				user_card.append(deal_card())
				user_score=calculate_score(user_card)

			else:
				is_game_over=True

	while dealer_score!=0 and dealer_score< 17:
		dealer_card.append(deal_card())
		dealer_score=calculate_score(dealer_card)

# FINAL RESULTS
	print(f"Your cards: {user_card}, current score: {user_score}")
	print(f"Computer's hands: {dealer_card}, final score: {dealer_score}")
# 	THE Winner LOGIC
	if user_score > 21:
		print("You went over. You lose! 😭")
	elif dealer_score > 21:
		print("Opponent went over. You win! 😁")
	elif user_score == dealer_score:
		print("It's a draw! 🙃")
	elif dealer_score == 0:
		print("Lose, opponent has Blackjack! 😱")
	elif user_score == 0:
		print("Win with a Blackjack! 😎")
	elif user_score > dealer_score:
		print("You win! 😃")
	else:
		print("You lose! 😤")


while input(f"Do you want to play Blackjack? Y or N?: ").lower()=="y":
	print("\n" *20)
	play_game()
