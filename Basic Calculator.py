import simpcalc

print("Welcome to the calculator!!!!")
num1 = int(input("Enter the  First number:")) 
num2 = int(input("Enter the  Second number:"))

print("Select the operators:\n 1.+ \n 2.- \n 3.* \n 4./")
select = int(input())

if select == 1:
    simpcalc.add(num1 , num2)
elif select == 2:
    simpcalc.sub(num1 , num2)
elif select == 3:
    simpcalc.multi(num1 , num2)
elif select == 4:
    simpcalc.div(num1 , num2)
else:
    print("Wrong Option")
input()

