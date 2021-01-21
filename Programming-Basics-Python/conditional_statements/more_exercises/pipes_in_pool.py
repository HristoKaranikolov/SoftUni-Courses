volume = int(input())
pipe_1_flow_rate = int(input())
pipe_2_flow_rate = int(input())
worker_missing_in_hours = float(input())

pipe_1_production = worker_missing_in_hours * pipe_1_flow_rate
pipe_2_production = worker_missing_in_hours * pipe_2_flow_rate
production_sum = pipe_1_production + pipe_2_production

if production_sum <= volume:
    production_percentage = production_sum / volume * 100
    first_productivity = pipe_1_production / production_sum * 100
    second_productivity = pipe_2_production / production_sum * 100
    print(f"The pool is {production_percentage:.2f}% full."
          f" Pipe 1: {first_productivity:.2f}%. Pipe 2:{second_productivity:.2f}%.")

else:
    overflows = production_sum - volume
    print(f"For {worker_missing_in_hours:.2f} hours the pool overflows with {overflows:.2f} liters.")
