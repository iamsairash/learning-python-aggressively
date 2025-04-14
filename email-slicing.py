# email slicing

email = input("Enter your email: ")
index = email.index("@")

emailName = email[:index]
domainName = email[index + 1:]

print(f"Your emailName is {emailName} and the domainName is {domainName}")