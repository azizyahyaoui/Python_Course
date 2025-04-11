print("---------------------------------------------------------------------------------------")

domain_names = ("gmail","hotmail","outlook","yahoo")

email = input("Enter the email to check: ")

if "@" in email and "." in email:
    domain = email.split('@')[1].split('.')[0]
    if domain in domain_names:
        print("Valid email!")
    else:
        print("Invalid domain. Supported domains are:", domain_names)
else:
    print("Invalid email format. Please ensure it contains '@' and '.'.")



print()
print("---------------------------------------------------------------------------------------")