def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if(n == 1):
        return 1
    if (n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(25))