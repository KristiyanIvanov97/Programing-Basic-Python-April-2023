pool_area = int(input())
first_pipe_debit = int(input())
second_pipe_debit = int(input())
hours_without_worker = float(input())

filled_area = hours_without_worker * first_pipe_debit + hours_without_worker * second_pipe_debit

filled_area_in_percent = filled_area / pool_area * 100
first_pipe_percent = hours_without_worker * first_pipe_debit / filled_area * 100
second_pipe_percent = hours_without_worker * second_pipe_debit / filled_area * 100

liters_overflow = filled_area - pool_area

if filled_area <= pool_area:
    print(f"The pool is {filled_area_in_percent}% full. Pipe 1: "
          f"{first_pipe_percent:.2f}%. Pipe 2: {second_pipe_percent:.2f}%.")
else:

    print(f"For {hours_without_worker} hours the pool overflows with {liters_overflow} liters.")








