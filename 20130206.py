'''
 (Intermediate): Base Conversion Words

Given as input an arbitrary string and base (integer), your goal is to convert the base-encoded string to all bases from 2 to 64 and try to detect all English-language words.

Author: aredna
Formal Inputs & Outputs
Input Description

On the console, you will be first given an arbitrary string followed by an integer "Base". This given string is base-encoded, so as an example if the string is "FF" and base is "16", then we know that the string is hex-encoded, where "FF" means 255 in decimal.
Output Description

Given this string, you goal is to re-convert it to all bases, between 2 (binary) to 64. Based on these results, if any English-language words are found within the resulting encodings, print the encoded string, the encoding base, and on the same line have a comma-separated list of all words you found in it.

It is ** extremely** important to note this challenge's encoding scheme: unlike the "Base-64" encoding scheme, we will associate the value 0 (zero) as the character '0', up to value '9' (nine), the value 10 as the character 'a' up to 35 as the character 'z', the value 26 as 'A', then the value 61 as 'Z', and finally 62 as '+' (plus) and 63 as '/' (division). Essentially it is as follows:

Values 0 to 9 maps to '0' through '9'
Values 10 to 35 maps to 'a' through 'z'
Values 36 to 61 maps to 'A' through 'Z'
Value 62 maps to '+'
Value 63 maps to '/'

Sample Inputs & Outputs
Sample Input

E1F1 22

Sample Output

Coming soon!

Challenge Input

None given
Challenge Input Solution

None given
Note

None
'''
mapping_table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
import sys

def convert_to_decimal(input, base):

	length = len(input)	
	decimal_value = 0	
	for (x, pos) in enumerate(range(length-1, -1, -1)):
		decimal_value +=  mapping_table.index(input[x]) * (pow(base, pos))	
	
	return decimal_value

def convert_decimal_to_base(decimal, base):
	number = ''	
	while (decimal / base != 0):
		number += mapping_table[decimal % base]
		decimal /= base
	number += mapping_table[decimal % base]
	return number[::-1]

if __name__ == '__main__':

	input_string = 'e1f1'
	input_base = 25 

	decimal_input = convert_to_decimal(input_string, input_base)
	
	for base in range(2,65):
		print ("base ", base, convert_decimal_to_base(decimal_input, base))
