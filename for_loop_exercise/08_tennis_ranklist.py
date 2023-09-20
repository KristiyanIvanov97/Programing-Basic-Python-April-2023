from math import floor

tournaments = int(input())
starting_points = int(input())

gained_points = 0
win_count = 0

for _ in range(tournaments):
    stage = input()
    if stage == "W":
        gained_points += 2000
        win_count += 1
    elif stage == "F":
        gained_points += 1200
    elif stage == "SF":
        gained_points += 720

total_points = starting_points + gained_points
average_points_per_tournament = floor(gained_points / tournaments)
percent_win_tournaments = win_count / tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points_per_tournament}")
print(f"{percent_win_tournaments:.2f}%")
