# Get a number on how many targets there will be.
targetNum = int(input("How many targets will there be: "))

# Create empty lists to hold information.
targetNameList = []
targetSurnameList = []
targetCompanyList = []

print("Please enter the target(s) first name, surname, and company.")

# loop through the number of requests and add each name to its list.
for i in range(targetNum):
    print("A new entry...")
    targetName = input("Name: ")
    targetSurname = input("Surname: ")
    targetCompany = input("Company: ")

    targetNameList.append(targetName)
    targetSurnameList.append(targetSurname)
    targetCompanyList.append(targetCompany)

print("Your email list has been generated.\n")

# email configurations
with open("companyemails.txt", "w") as f:
    for i in range(targetNum):
        f.write(f"{targetNameList[i]}.{targetSurnameList[i]}@{targetCompanyList[i]}.com\n")
        f.write(f"{targetSurnameList[i]}.{targetNameList[i]}@{targetCompanyList[i]}.com\n")
        f.write(f"{targetNameList[i][0]}.{targetSurnameList[i]}@{targetCompanyList[i]}.com\n")

# close the file
f.close()
