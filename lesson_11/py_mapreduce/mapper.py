import sys

# inout comes from STDIN (standard input)
for line in sys.stdin:

    line = line.strip() # remove leading and trailing whitespaces
    words = line.split() # split line into words

    for word in words:
        print('%s\t%s' % (word,1))
