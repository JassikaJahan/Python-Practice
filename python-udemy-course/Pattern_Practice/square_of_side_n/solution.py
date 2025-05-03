def generate_square(n):
    square = []
    
    for i in range(n):
        square.append('*' * n)
    
    return square


square = generate_square(5)
print(square)
