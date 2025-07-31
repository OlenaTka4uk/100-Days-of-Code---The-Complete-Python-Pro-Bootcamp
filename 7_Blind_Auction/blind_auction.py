import random
import logo

print(logo.logo)

number_of_users = random.randint(2, 10)
users = {}

while number_of_users > 0:
    name = random.choice(['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'])
    bid = random.randint(50, 1000)
    users[name] = bid
    number_of_users -= 1

user_name = input("What is your name? ")
user_bid = int(input("What is your bid (from $50 till $1000)? $"))
users[user_name] = user_bid

def find_highest_bidder(users):
    highest_bid = 0
    winner = ""

    for user in users:
        if users[user] > highest_bid:
            highest_bid = users[user]
            winner = user

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

find_highest_bidder(users)
