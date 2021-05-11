#  the program checks the factorial of a given number 
#  define the function, then evaluate that the number is greater than 0, else return 1.
def fact(x):
    if x == 0:
        return 1
    #  will multiply recursively
    return x * fact(x - 1)

x=int(input("Number to compute factorial:"))
print (fact(x))