from replit import clear
#HINT: You can call clear() to clear the output in the console.
# from art import logo
# print(logo)

# print("Welcome to secret auction and good luck.")
# def get_name_bid(): 

#   name_and_bids = {
#     "name": input("What is your name? "), 
#     "bid": input("What is your bid? $ ")
# }
# print("$ " + name_and_bids["bid"])

# bidders_list = {}

# play_again = input("Do you want to bid? Type 'yes' if you want, else type 'no'.")
# if play_again == "yes":
#   clear()
#   get_name_bid
# else:
#   print(highest_bidder)

# Angela's Solution
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name? ")
  price = int(input("What is your bid? $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
