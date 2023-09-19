import random
import numpy as np
######################## 40095 or 191692
k = 500
########################
output_symbols = [2] * k
output_symbols_count = 0
def generate_random_sequence(seed_value, deg):
    random.seed(seed_value)
    min_value = 1
    max_value = k
    possible_values = list(range(min_value, max_value + 1))
    random_sequence = random.sample(possible_values, deg)
    return random_sequence

def LTcode_decoding(matrices):   
    n = len(matrices)
    decoding_dict = {i: [] for i in range(n)}
    encoded_symbols = [0] * n
    degrees = [0] * n
    
    # degree and encoding_symbol
    for i in range(n):
        degrees[i] = matrices[i][0]
        encoded_symbols[i] = matrices[i][1]
        
        seed_value = int(matrices[i][2])
        deg = matrices[i][0]
        random_sequence = generate_random_sequence(seed_value, deg)
        
        for index in random_sequence:
            decoding_dict[i].append(index)
    
    while not all(deg != 1 for deg in degrees):
        for i in range(n):
            if degrees[i] == 1 and len(decoding_dict[i]) != 0:  
                j = decoding_dict[i][0]
                output_symbols[j - 1] = encoded_symbols[i] 
                degrees[i] -= 1
                decoding_dict[i].remove(j)
                        
                for l in range(n):
                    if j in decoding_dict[l]:
                        degrees[l] -= 1
                        decoding_dict[l].remove(j)
                        encoded_symbols[l] ^= encoded_symbols[i]
        
    return output_symbols


