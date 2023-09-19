import numpy as np
import random
import math
import time
from main import main
from main_gray import main_gray
c=0.15
delta=0.2
data = ''
#####################
output=main_gray()
for i in output:
    data += i
k=len(data)

# k=6400
#####################
def generate_random_sequence(seed_value, deg):
    random.seed(seed_value)
    min_value = 1
    max_value = k
    possible_values = list(range(min_value, max_value + 1))
    random_sequence = random.sample(possible_values, deg)
    return random_sequence

def lt_encoding(input_symbols):
    k = len(input_symbols)
    CDF_matrix = [0] * (k + 1)
    CDF_matrix[1] = 1 / k
    for i in range(2, k + 1):
        CDF_matrix[i] = CDF_matrix[i - 1] + (1 / (i * (i - 1)))

    R = c * math.log(k / delta) * math.sqrt(k)
    CDF_matrix2 = [0] * (k + 1)
    G = int(k / R + 0.5)

    for i in range(1, G - 1):
        CDF_matrix2[i] = R / (i * k) + CDF_matrix2[i - 1]
    CDF_matrix2[G] = (R * math.log(R / delta)) / k + CDF_matrix2[int(k / R) - 1]
    for i in range(G + 1, k + 1):
        CDF_matrix2[i] = 0 + CDF_matrix2[i - 1]
    
    Beta = CDF_matrix[k] + CDF_matrix2[k]
    CDF_matrix = [(x + y) / Beta for x, y in zip(CDF_matrix, CDF_matrix2)]
    number=0
    while True:
        random_numbers = random.random() 
        for i in range (k):
            if random_numbers <= CDF_matrix[i]:
                deg = i             
                break
        scaled_time = number % 65536
        seed_value = (scaled_time ) % 65536
        random_sequence = generate_random_sequence(seed_value, deg)
        number+=1
        a = 0
        for i in range(deg):
            index = random_sequence[i]
            a += input_symbols[index-1]
            encoded_symbols = a % 2

        print(deg,  encoded_symbols, seed_value)

 #input_symbols = [random.randint(0, 1) for _ in range(160)]

# number=0
# seed = 0
# while True:
#     seed = (number)% 65536
#     number+=1
#     deg, encoded_symbols, seed_value = lt_encoding(input_symbols, seed)
#     # print(deg, encoded_symbols, seed_value)
