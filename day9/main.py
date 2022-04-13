from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art

bid_again = True
bidDict = {}

def user_inputs():
    name= input("What is your name?: ")
    bid= input("What's your bid?: $")

    bidDict[name] = bid

def highest_bidder():
  max_key = None
  max_val = None

  for key, val in bidDict.items():
    if max_val is None or val > max_val:
        max_val = val
        max_key = key

  return max_key, max_val

print(art.logo)
user_inputs()

while bid_again:
    restart_bid = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if restart_bid.lower() == 'no':
        bid_again = False
        winner, value = highest_bidder()
        print("Bidding done!")
        print("The winner is %s with a bid of $%s" % (winner, value))
    else:
        clear()
        user_inputs()
