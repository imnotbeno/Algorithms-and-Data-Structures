# !python3

# Memoization of nth fibonacci number, using a lookup table

def fib(n, lookup):

    # bas case
    if n == 0 or n == 1:
        lookup[n] = n

    # if the value is not in the lookup array, calculate it and store it 
    if lookup[n] is None: 
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
    
    return lookup[n]

def main():
    n = 4

    lookup = [None] * 101
    print ("Fibonacci number is: ", fib(n, lookup))

main()


