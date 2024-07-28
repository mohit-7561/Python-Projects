import os
def findingBinod(filename):
    with open(filename, "r") as f:
        readFile = f.read()
    if "binod" in readFile.lower():
        return True
    else:
        return False
if __name__=="__main__":
    countBinod = 0
    fileNames = os.listdir()
    for item in fileNames:
        if item.endswith(".txt"):
            print(f"Finding Binod in {item}")
            spam = findingBinod(item)
            if spam:
                print(f"*********binod found in {item}********")
                countBinod += 1
            else:
                print(f"binod not found in {item}")

print("------Spam Words Details------")
print(f"{countBinod} spams found in them")
