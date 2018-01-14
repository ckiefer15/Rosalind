def rabbitRecurrence(n):
    if n==0 or n==1 or n==2:
        return 1
    return (rabbitRecurrence(n-1) + k * rabbitRecurrence(n-2))

count = 0

# number of offspring produced by each pair that can mate
k = 2
#number of months
n=28

count = rabbitRecurrence(n)
print(count)