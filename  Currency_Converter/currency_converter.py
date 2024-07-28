with open("currency.txt") as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    currency = line.split("\t")
    currencyDict[currency[0]] = currency[1]
    
amount = int(input("Enter the amount: "))
print("Choose the currency given below:")
for item in currencyDict.keys():
    print(item)
currencyNote = input("Enter the currency: ")
print(f"{amount} INR is equal to {amount * float(currencyDict[currencyNote])} {currencyNote}")