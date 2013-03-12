__author__ = 'appell'


input = 7

history = {}

def count_coins(denomination):
    if (history.has_key(denomination)):
        print "re-using ", denomination, " result is ", history[denomination]
        return history[denomination]
    elif (denomination == 0):
        return 1
    else:
        ret_val = count_coins(denomination/3) + count_coins(denomination/2) + count_coins(denomination/4)
        history[denomination] = ret_val
        return ret_val

print(count_coins(input))

print history
