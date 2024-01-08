#[Find the Factorial of a Number] 16

#factorial number> 5!=5*4*3*2*1 = 120(5! ar factorial)

#solution-1 using for loop
 
# num = int(input("enter a number here: "))

# fact = 1

# if num < 0 :
#     print("factorial of 0 dose not exist")
# if num == 0:
#     print("factorial of 0 is",  1)
# if num > 0:
#     for i in range (1,num+1) :
#         fact = fact * i
# print("the factorial of the given number is", fact)
  

#Solution 2 using recursion

def fact(a):
    if a  == 0:
        return 1
    else:
        return ((a)*fact(a-1))
    
num = int(input("enter a number here: "))

result = fact(num)
print("the factorial of the given number is", result)
