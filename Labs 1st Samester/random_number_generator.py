# Initializing the seed
seed = 1

def custom_random():
    global seed
    # These constants are used in the LCG algorithm
    a = 1103515245
    c = 12345
    m = 2 ** 31

    # LCG algorithm to generate pseudo-random numbers
    seed = (a * seed + c) % m
    return seed % 20 + 1  # Return a random number between 1 and 20

# Testing the custom_random function
for _ in range(10):
    print(custom_random())
