def calculate_lift_rounds(n, capacity):
    round = n//capacity
    if n % capacity != 0:
        round += 1
    return round 
   

max_turn = calculate_lift_rounds(10, 3)
print(max_turn)