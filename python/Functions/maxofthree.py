def maxOfThree(x,y,z):

    if x>=y and x>=z:
        return x
    elif y>=x and y>=z:
        return y
    else:
        return z

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
maximum=maxOfThree(num1,num2,num3)
print("Maximum number is:", maximum)