def fiboIterative(n):
    previousNum = 0
    currentNum = 1
    for i in range(1, n):
        prePreviousNum = previousNum
        previousNum = currentNum
        currentNum = prePreviousNum + previousNum
    return currentNum

def fiboRecusrive(n):
    if n==0:
        return 0 
    elif n==1:
        return 1
    else:
        return fiboRecusrive(n-1) + fiboRecusrive(n-2)

if __name__=="__main__":
    user = int(input("Enter a number:\n"))
    # print(f"the fibonacci recusrive of {user} is {fiboRecusrive(user)}")
    print(f"the fibonacci iterative of {user} is {fiboIterative(user)}")

