target_steps = 10000

total_steps = 0

while True:
    command = input()
    if command == "Going home":
        daily_steps = int(input())
        total_steps += daily_steps
        break

    daily_steps = int(command)
    total_steps += daily_steps

    if total_steps >= target_steps:
        break

if target_steps <= total_steps:
    print(f"Goal reached! Good job!\n{total_steps - target_steps} steps over the goal!")
else:
    print(f"{target_steps - total_steps} more steps to reach goal.")
