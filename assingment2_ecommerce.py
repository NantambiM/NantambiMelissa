
users={
    "admin": "admin123",
    "customer1": "iamacustomer",
    "cashier":"password"
}
attempts=0
max_attempts=3

print("Welcome to the E-commerce System!")

while attempts<max_attempts:
    username=input("Enter your username: ")
    password=input("Enter your password: ")

    if username in users and users[username]==password:
        print("Login successful!")

        if(username=="admin"):
            print("Welcome, Admin! You have full access to the system.")
        elif(username=="customer1"):
            print("Welcome, Customer! You can browse products and make purchases.")
        elif(username=="cashier"):
            print("Welcome, Cashier! You can process transactions.")

        break

    elif(username in users and users[username]!=password):
            print("Invalid password.")
    else:
        print("User not found")

    attempts+=1


coupon_code=input("Enter a coupon code: ")
sub_total=int(input("Enter the sub total: "))
location=input("Enter your location: ")
coupon_code_valid=True

if sub_total>500000:
    discount=10
elif sub_total>250000:
    discount=7
elif sub_total>100000:
    discount=5
else:
    discount=0

if(coupon_code):
    if(coupon_code_valid):
        print("Your coupon is valid") 
        if(discount):
            actual_discount=sub_total*(discount/100)
        else:
            print("You don't get any discount")
            actual_discount=0
    else:
        print("Coupon is invalid")
else:
    print("You have no coupon")

total=sub_total-actual_discount


if location=="Kampala":
    tax=12
    actual_tax=sub_total*(tax/100)
else: 
    tax=5
    actual_tax=sub_total*(tax/100)


total+=actual_tax
print(f"Your total is {total}")

