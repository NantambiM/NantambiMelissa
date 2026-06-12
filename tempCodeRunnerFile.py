#actual system assignment
users={
    "admin": "admin123",
    "customer1": "cust123",
    "cashier":"password"
}

print("Welcome to the E-commerce System!")
username=input("Enter your username: ")
password=input("Enter your password: ")

if username in users and users[username]==password:
    print("Login successful!")

