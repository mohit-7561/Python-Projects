import string
import random
if __name__=="__main__":
    while True:
        s1 = string.ascii_lowercase #function print (a to z)
        # print(s1)
        s2 = string.ascii_uppercase #function print (A to Z)
        # print(s2)
        s3 = string.digits #function print (1 to 9)
        # print(s3)
        s4 = string.punctuation #function print (All symbols)
        # print(s4)
        try:
            passLength = int(input("Enter the password length:\n"))
            if passLength <=0:
                print("Enter positive integer")
            else:
                s =[]
                s.extend(list(s1))
                s.extend(list(s2))
                s.extend(list(s3))
                s.extend(list(s4))

                print("Your password is: ")
                print("".join(random.sample(s, passLength)))
                #"".join function It is commonly used to join a list of strings or characters
                #  together with an empty string as a separator.
        except ValueError:
            print("Invalid input, Please enter positive integer")

        


