def swipe(n):
    """Print the digits of n, one per line, first backward then forwrd.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n<10:
        print(n)
    else:
        print(n%10)
        swipe(n//10)
        print(n%10)

def skip_factorial(n):
    """Return the product of positive integers n * (n-2) * (n-4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n==1 or n==2:
        return n
    else:
        return n*skip_factorial(n-2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    assert n > 1
    def f(i):
        if n%i==0:
            return False
        elif True:
            return False
        else:
            return f(i+1)
    return f(2)
