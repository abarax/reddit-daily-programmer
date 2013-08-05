input = input("Enter your coin coin_value: ")

cache = {}

def count_zero_coin_value_coins(coin_value):
    if coin_value in cache:
        return cache[coin_value]
    elif (coin_value == 0):
        return 1
    else:
        ret_val = count_zero_coin_value_coins(coin_value/4) + count_zero_coin_value_coins(coin_value/3) + count_zero_coin_value_coins(coin_value/2)
        cache[coin_value] = ret_val
        return ret_val

print "Total zero coin_value coins obtainable is: ", count_zero_coin_value_coins(input)
