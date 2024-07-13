
def Fibonacci(n):
    if n <= 0:
        return 0

    elif n == 1:
        return 1

    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# Driver Program
n=int(input())
sum=0
for i in range(1,n+1):
   sum=sum+(Fibonacci(i)*Fibonacci(i))

print (sum)