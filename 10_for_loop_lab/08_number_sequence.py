import sys

smallest = sys.maxsize
biggest = -sys.maxsize
numbers_count = int(input())

for i in range(0, numbers_count):
    number = int(input())
    if number < smallest:
        smallest = number
    if number > biggest:
        biggest = number

print(f"Max number: {biggest}\nMin number: {smallest}")
