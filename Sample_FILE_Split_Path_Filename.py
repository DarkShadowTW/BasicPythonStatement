import os

def gfuc_split_path_file(fullpath):
    pathname, filename = os.path.split(fullpath)
    print(pathname)
    print(filename)

def gfuc_split_file_extend(fullpath):
    path_element = os.path.splitext(path)
    print(path_element[1])

def gfuc_split_file(fullpath):
    path_element = os.path.basename(path)
    print(path_element)

# Windows PATH
path = 'c:\\workarea\\filename.py'
gfuc_split_path_file(path)
gfuc_split_file_extend(path)
gfuc_split_file(path)