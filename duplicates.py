import os
import sys
from collections import defaultdict, namedtuple


File = namedtuple('File', 'name size')

def walk(directory):

    dict_of_path = defaultdict(list)

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(full_path)
            file = File(filename, file_size)
            dict_of_path[file].append(full_path)
    return dict_of_path


def print_duplicates(dict_of_path):
    for file in dict_of_path:
        if len(dict_of_path[file]) > 1:
            print('Filename:', file.name, '/ size', file.size, 'bytes')
            print('-' * 50)
            for path in dict_of_path[file]:
                print(path)
            print('-' * 50,'\n')


if __name__ == '__main__':
    
    if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
        filepath = sys.argv[1]
        dict_of_path = walk(filepath)
        print_duplicates(dict_of_path)
    else:
        print("Path not found.")
        print("Example launch: python duplicates.py <path>")