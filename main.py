import random
import sys

numbers = '0123456789'
literals = 'abcdefghijklmnopqrstuvwxyzß'
cap_literals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
extras = '!?.,_-#*+$%&/()=<>'

listOfArguments = [numbers,
                   literals,
                   cap_literals,
                   extras]

length = int(sys.argv[1])
if len(sys.argv) < 2:
    exit('No length input!')

if length < 8:
    print('Longer password recommended!')

password = ''
for x in range(0, length):
    password += random.choice(random.choice(listOfArguments))
print(password)
