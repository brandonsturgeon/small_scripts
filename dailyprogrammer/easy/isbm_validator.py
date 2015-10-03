# https://www.reddit.com/r/dailyprogrammer/comments/2s7ezp/20150112_challenge_197_easy_isbn_validator/
# Brandon Sturgeon

from sys import argv

# Quick #
print sum([(10-k)*int(number) for k, number in enumerate(list(argv[1].replace("-","")))]) % 11 == 0

# Long #

# Get the number as a system argument
given_number = argv[1]

# Get rid of -'s and split it into a list of characters
exploded = list(given_number.replace("-", ""))

# Get all of the multiplied values
values = []

# Loop through key,value of exploded string
# Convert each character to a number, and
# multiply it by 10-key
# (We want 0'th element multiplied by 10, 9th element multiplied by 1)
for key, number in enumerate(exploded):
    multiplied = (10-key)*int(number)
    values.append(multiplied)

the_sum = sum(values)

if the_sum % 11 == 0:
    print "Valid ISBN Number!"
else:
    print "Invalid ISBN Number!"
