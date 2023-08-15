import os

from art import logo

print(logo)
another_user_bidding = True
bids = {}
while another_user_bidding:
    name = input("What is your name?")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    query = input("Any other user want to bid? Enter 'yes' or 'no'")
    if query.lower() == "no":
        another_user_bidding = False
    elif query.lower() == "yes":
        os.system("cls")


def highest_bidder():
    highest_bid = 0
    winner_name = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner_name = bidder
    print(f"The winner is {winner_name} with the highest bid of ${highest_bid}")

highest_bidder()