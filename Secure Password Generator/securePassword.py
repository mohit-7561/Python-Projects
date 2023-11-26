secure = (("a", "@"), ("b", "8"), ("c", "("), ("e", "3"), ("g", "6"),("h", "#"),("i", "!"), ("l", "1"),("o", "0"), ("s", "$"), ("t", "+"), ("x", "%"))

def securePassword(password):
    for a,b in secure:
        password = password.replace(a,b)
    return password


if __name__=="__main__":
    while True:
        password = input("Enter your password:\n")
        password = securePassword(password)
        print(f"Your secure password is: {password}")