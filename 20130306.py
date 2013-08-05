input = input("Enter your coin value: ")

cache = {}

def obtain_max_value(coin_value):
    if coin_value in cache:
        return max(cache[coin_value], coin_value)
    elif coin_value == 0:
        cache[coin_value] = 0
        return 0
    else:
        ret_val = obtain_max_value(coin_value/4) + obtain_max_value(coin_value/3) + obtain_max_value(coin_value/2)       
        cache[coin_value] = ret_val

    return max(coin_value, ret_val)

print "The max value obtainable is: ", obtain_max_value(input)
