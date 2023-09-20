Hours_Per_Project = 3

architecture_name = input()
projects = int(input())

hours_needed = projects * Hours_Per_Project

print(f"The architect {architecture_name} will need {hours_needed} hours to complete {projects} project/s.")