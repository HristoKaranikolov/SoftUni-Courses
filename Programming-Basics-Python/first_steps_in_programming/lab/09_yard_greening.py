size_in_metres = float(input())

cost_per_sq_meter = 7.61

total_cost = size_in_metres * cost_per_sq_meter

discount = total_cost * 0.18
final_price = total_cost - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")