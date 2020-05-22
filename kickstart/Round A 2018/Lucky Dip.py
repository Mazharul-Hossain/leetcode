import numpy as np 

def lucky_dip(N, K, item_value):
    if N == 0:
        return 0
    elif N == 1:
         return item_value[0]
    elif K == 0:
        return np.sum(item_value) / N

    item_hash = {}
    item_value.sort(reverse=True)
    for item in item_value:
        if item not in item_hash:
            item_hash[item] = 0
        item_hash[item] += 1
    
    if len(item_hash) == 1:
        return item_value[0]

    likely_value, probability, N1 = 0.0, 1, N    
    for item, count in item_hash.items():
        probability_1 = probability * ( ( N1-count ) / N ) ** (K + 1)
        
        likely_value += item * (probability - probability_1)
        probability, N1 = probability_1, N1 - count
        
    return "%.9f" % likely_value


def main():
    T = int(input())
    for case in range(1, T + 1):
        input_string = input()
        N, K = input_string.split()
        N, K = int(N), int(K) 
        
        input_string = input()
        item_value = list(map( int, input_string.split() )  )
        print("Case #", case, ": ", lucky_dip(N, K, item_value))

if __name__ == '__main__':
    main()
