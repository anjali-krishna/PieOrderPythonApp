print("Welcome to the House of Pies! Here are our pies:")
print("-"*45)
run ="y"
pieCart = []
piePurchase = [0,0,0,0,0,0,0,0,0,0]
while(run == "y"):
    pies = ["Pecan","Apple Crisp","Bean","Banoffe","Black Bun","Blueberry","Buko","Burek","Tamale","Steak"]
    for pie in pies:
        print("["+str((pies.index(pie))+1)+"]"+pie)
    pie_selected = int(input("Select the pie you'd like to order via number: "))
    print("Great! We'll have that "+pies[pie_selected-1]+" right out for you.")
    pieCart.append(pies[pie_selected-1])
    piePurchase[pie_selected-1] = piePurchase[pie_selected-1]+1
    run = input("Would you like to make another order(yes/no): ")
    if(run == "n"):
        print("The total number of pies ordered: "+str(len(pieCart)))
        print("You Purchased:")
        for pie in pies:
            print(str(piePurchase[pies.index(pie)])+" "+pie)
