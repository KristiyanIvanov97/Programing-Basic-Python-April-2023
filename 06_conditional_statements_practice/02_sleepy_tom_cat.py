days_off = int(input())
NORM_FOR_PLAY = 30000

working_days = 365 - days_off
time_in_minutes = working_days * 63 + days_off * 127

difference_in_game_norm = 30000 - time_in_minutes

hours = abs(difference_in_game_norm) // 60
minutes = abs(difference_in_game_norm) % 60

if NORM_FOR_PLAY < time_in_minutes:
    print(f"Tom will run away\n{abs(hours)} hours and {minutes} minutes more for play")
elif time_in_minutes < NORM_FOR_PLAY:
    print(f"Tom sleeps well\n{hours} hours and {minutes} minutes less for play")
