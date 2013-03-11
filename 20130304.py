__author__ = 'abarax'


input = 7

def count_coins(denomination):
    if (denomination == 0):
        return 1
    else:
        return count_coins(denomination/3) + count_coins(denomination/2) + count_coins(denomination/4)

print(count_coins(input))
