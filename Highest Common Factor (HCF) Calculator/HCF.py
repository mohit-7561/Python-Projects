num1 = int(input("Enter number 1:\n"))
num2 = int(input("Enter number 2:\n"))

min_num = min(num1, num2)

for i in range(1, min_num+1):
    if num1%i ==0 and num2%i ==0:
        HCF = i

print(f"The HCF of the {num1} and {num2} is {HCF}")