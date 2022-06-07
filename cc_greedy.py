#Coin Change Using Greedy
#Minimum no of coins

amt = int(input("Enter initial amount : "))
den = [int(item) for item in input("Enter Denominations : ").split()]
coins = []

den = sorted(den , reverse=True)

while(amt!=0):
    
    for i in range(0,len(den)):
        while(amt>=den[i]):
            amt-= den[i]
            coins.append(den[i])

print(coins)
