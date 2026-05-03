# TODO-1: Ask the user for input

bidding_dictionary = {}
def highest_bidder(bidding_record):
    maximum_bid = 0
    winner =""
    for keys in bidding_record:
        bid_amount = bidding_record[keys]
        if bid_amount > maximum_bid:
            maximum_bid = bid_amount
            winner = keys
    print(f"The winner is {winner} with the highest bid of {maximum_bid}")

# TODO-2: Save data into dictionary {name: price}
max_bid = 0
is_new_bid = True
while is_new_bid:
    bidder_name = input("What's your name?")
    bidding_price = int(input("How much do you want to bid?"))
    new_bidder = input("Is there anyone who want to bid anymore? Press 'Yes' to bid otherwise 'No' to close")

    bidding_dictionary[bidder_name] = bidding_price
    if new_bidder == "No":
        is_new_bid = False
        highest_bidder(bidding_dictionary)
    elif new_bidder == "Yes":
        print("\n" * 20)



# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


