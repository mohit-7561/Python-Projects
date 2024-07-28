user = int(input("Enter the number:\n"))
sum = 0
save_user = user
order = len(str(user))
while(user>0):
    digit = user%10 # this method used to give the remainder same as the last
    #digit of the number, ex: 8891 it will give 1 and so on
    sum = sum+ digit**order 
    user = user//10 #this method used to give the before decimal number
    #ex: 8891//10, 889.1 give 889 and so on
if (save_user == sum):
    print(f"{save_user} is a armstrong number")
else:
    print(f"{save_user} is not an armstrong number")