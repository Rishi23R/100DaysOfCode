from replit import clear
from art import logo
# You can call clear() to clear the output in the console.

def register_bids():
    try:
        name = input('name please\n')
        bid = input('your bid?\n')
        bids[name]=int(bid)
    except ValueError:
        print('please enter integer values only for bid')

bids={}
repeat=True

print('welcome to the bidding\n')
print(logo)
count=0
while repeat:
   clear()
   register_bids()
   should_repeat=input('do you see other bidders in the room').lower()
   if should_repeat=='no':
        repeat=False
max_bid=max(bids.values())
for key,value in bids.items():
    if value==max_bid:
        max_bid_name=key
        break
print(f'winner is {max_bid_name} with bid value {max_bid}')
