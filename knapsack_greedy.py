n = int(input("Enter no of items : "))
m = int(input("Enter max Capacity of Bag : "))
cap=0

items = []
selected= []
profit=0

for i in range(0,n):
    vi=int(input(f"Enter value of Item {i+1} : "))
    wi=int(input(f"Enter Weight of Item {i+1} : "))
    items.append({"name": f"Item {i+1}" , "pr" : round((vi/wi) , 2) , "w":wi , "v":vi})

items = sorted(items , key=lambda x : x['pr'] , reverse=True)


for item in items:
        if item['w']<= m-cap:
            selected.append(item['name'])
            profit+=item['v']
            cap+=item['w']
        else:
            frac = (m-cap)/item['w']
            profit+= item['v']*frac
            selected.append(f"{item['name']} ({frac})")
            cap=m
            break
    
print(selected)
print(profit)
