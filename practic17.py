#[Display the multiplication Table] 17
#solution 1 with for loop

n = int(input("enter a number here:"))

for i in range(1,11):
    print (n,  "x", i,"=",n*i)
