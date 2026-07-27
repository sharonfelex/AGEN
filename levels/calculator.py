print("===== CALCULATOR =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


choice= int(input("enter your values:"))

num1=int(float(input("enter your first number:")))
num2=int(float(input("enter your second number:"))) 

if choice==1:
    print(num1,"+",num2,"=",num1+num2)
elif choice==2:     
    print(num1,"-",num2,"=",num1-num2)
elif choice==3: 
    print(num1,"*",num2,"=",num1*num2)
elif choice==4:
    print(num1,"/",num2,"=",num1/num2)    
else:
    print("invalid input")
    