
var=2018
word= "This is a Simple Calculator"
print("Game On Python!!!!!", var, word)
print("Enter two digits you want to Compute")
a= int(input("Enter Value Of First Digit"))
b= int(input("Enter Value Of Second Digit"))
op= input("Enter Operator")
if (op== "+"):
    print(a+b)

elif (op== "-"):
    print(a-b)

elif (op== "*"):
    print(a*b)

elif (op== "/"):
    print(a/b)

else:
    print("Invalid Operator")
