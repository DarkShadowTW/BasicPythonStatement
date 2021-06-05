import os

source_dir = ['C:\\workarea\\CShap']

#遞迴呼叫
def scan_dictionary(dict):
    if os.path.isdir(dict):
        for element in os.listdir(dict):
            fullpath = os.path.join(dict, element)
            scan_dictionary(fullpath)
    else:
        print(dict)

for element in source_dir:
    scan_dictionary(element)
