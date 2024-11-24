n = int(input("Enter a number: "))
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(f"Factorial of {n} is {factorial(n)}")




'''
Old code:

n = 8
def fib(n):
	if n <= 1:
	    return n
	else:
		return fib(n-1) + fib(n-2)

'''

