import random
import logo

print(logo.logo)

computer_bid = random.randint(50, 1001)

user_name = input("What is your name? ")
user_bid = int(input("What is your bid (from $50 till $1000)? $"))

def find_highest_bidder():
    if user_bid > computer_bid:
        print(f"{user_name} is winner with a bid of {user_bid}. Another bid was {computer_bid}")
    elif user_bid == computer_bid:
        print("The same bid")
    else:
        print(f"Sorry, but we have another winner with the bid of {computer_bid}!")

find_highest_bidder()
