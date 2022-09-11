'''
Author: Shawn C
Date: 2022-09-11 17:10:48
FilePath: ./Blind-Auction/main.py
'''
def logo():
    print("""
    Hello there! This is Shawn.
    ░░░░░░░░░░▄▀▄░░░░░▄▀▄░░░░░░░░░░
    ░░░░░░░░░▄█░░▀▀▀▀▀░░█▄░░░░░░░░░
    ░░░░░▄▄░░█░░░░░░░░░░░█░░▄▄░░░░░
    ░░░░█▄▄█░█░░▀░░┬░░▀░░█ █▄▄█░░░░
    """)

user_bids = {}
bidding_end = False

def high(bidding_log):
    high_bid = 0
    won = ""
    for bidder in bidding_log:
        user_bids = bidding_log[bidder]
        if user_bids > high_bid:
            high_bid = user_bids
            won = bidder   
    print(f"With bid of ${high_bid}, Congratulations! The WInner is {won}.")

while not bidding_end:
    print("\n" * 100)
    logo()
    name = input("Your name:\n>> ")
    bid = int(input("Your bid:\n>> $"))
    user_bids[name] = bid
    add_bidders = input("Participant?\n>> ").lower()
    if add_bidders == "n":
        bidding_finished = True
        high(user_bids)
        break


