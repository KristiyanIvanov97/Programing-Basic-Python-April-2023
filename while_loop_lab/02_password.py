username = input()
correct_password = input()
current_password = input()

while current_password != correct_password:
    current_password = input()
print(f"Welcome {username}!")