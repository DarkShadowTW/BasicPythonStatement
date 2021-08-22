#The content of data/data.txt
#   LINE - 1
#      LINE - 2
#LINE - 3

with open('data/data.txt') as f:
    for line in f.readlines():
        print(line)
    #OUTPUT
    #   LINE - 1
    #
    #    LINE - 2
    #
    #LINE - 3
    #

with open('data/data.txt') as f:
    for line in f.readlines():
        print(line.strip())
    #OUTPUT
    #LINE - 1
    #LINE - 2
    #LINE - 3

#LIST = [Variant for Variant in Dataset if Statement]
with open('data/data.txt') as f:
    labels = [line for line in f.readlines()] #strip() 去除首尾空格                       #?????

print(labels)
# OUTPUT - ['LINE - 1', 'LINE - 2', 'LINE - 3']
