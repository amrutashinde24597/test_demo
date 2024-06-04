x= int(input("Enter any number between 40 to 100 :"))
if x<40:
    print(x,"less than 40")
elif x in range(40,100):
    print("Vallid:")
else:
    print(x,"is out of range")