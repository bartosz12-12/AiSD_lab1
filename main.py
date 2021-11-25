def numbers(n : int):
    if n < 0:
        return
    print(n)
    numbers(n-1)



def fib(n : int):
    if n == 0:
        return 0
    if n == 1:
        return 1

    else:
        return  fib(n-1) + fib(n-2)

def power(num : int, n : int):
    if(n == 0):
        return 1
    else:

            return num * power(num, n-1)

def reverse(txt):
    if len(txt) == 0:
        return txt
    else:
        return reverse(txt[1:]) + txt[0]

def factorial(n:int):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
