# writing some functions in python

num1 = 15 
num2 = 3

def addtions():
    # sum
    sum = num1 + num2
    print(sum)
    # sub
def subtraction():
    sub = num1 - num2 
    print(sub)
    # multiply 
def multiplication():
    mul = num1 * num2 
    print(mul)
    # division 
def divesion():
    div = num1 / num2
    print(int(div))
# call the functions 
addtions()
subtraction()
multiplication()
divesion()
################################################################################
# writing second function 
def num_addtions(num5, num6):
    # sum
    sum1 = num5 + num6
    return(sum1)
    # sub
def num_subtraction(num5,num6):
    sub1 = num5 - num6 
    return(sub1)
def num_multiplication(num5, num6):
    # multiply 
    mul1 = num5 * num6 
    return(mul1)
    # division
def num_divesion(num5, num6):
    div1 = num5 / num6
    return(div1)
# call function with number 
Number1 = num_addtions(45, 5)
print(Number1)
Number2 = num_subtraction(45, 5) 
print(Number2)
Number3 = num_multiplication(45, 5) 
print(Number3)
Number4 = num_divesion(45, 5) 
print(int(Number4))

###################################################################

# function with two arguments
def add_numbers(num3, num4):
    sum = num3 + num4
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4)
###################################################
# writing squre
def num_squre(num):
    sq = num * num
    return(sq)
# function call with value
Square = num_squre(9)
print("number: ", Square )
