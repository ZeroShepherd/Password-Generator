import random
import re

print("Performing calculation of a random password\n")
x = input("How long would you like your random password to be?\n")
x = int(x)

lower_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

all = []
all = lower_a + upper_a + num + chars

subThis = (str(random.choices(all, k=x)))
print(re.sub('\'|\,|\[|\]|\ ', '', subThis))
