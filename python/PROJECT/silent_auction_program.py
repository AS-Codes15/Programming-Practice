import os
print("***Welcome to the silent auction program***")
def  find_winner(bidder_dtails):
    highest_bid=0
    winner=""
    for bidder in bidder_dtails:
        bidding_price=bidder_dtails[bidder]
        if bidding_price > highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f"Here is the details of all the bidders: {bidder_dtails}")        
    print(f"The winner is {winner} with a bid price of {highest_bid}")        

bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("What is your name?: ")
    price=int(input("What is your bid?: "))
    bidder_data[name]=price
    more_bidder=input("Are there more bidder? Type 'yes' or 'no': ").lower()
    if more_bidder=='no':
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidder=='yes':
        os.system('cls')


