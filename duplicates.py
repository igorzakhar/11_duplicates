import os
import sys
import hashlib
from collections import defaultdict, namedtuple


File_object = namedtuple('File', 'name size checksum')


def md5_checksum(filename, blocksize=65536):
    checksum = hashlib.md5()
    with open(filename, 'rb') as fp:
        buffer = fp.read(blocksize)
        while len(buffer) > 0:
            checksum.update(buffer)
            buffer = fp.read(blocksize)
    return checksum.hexdigest()


def enumerate_path(path = '/tmp/duplicates'):
    path_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fulpath = os.path.join(dirpath, f)
            path_collection.append(fulpath)
    return path_collection


def get_duplicates(path_collection):
    records  = defaultdict(list)
    for file in path_collection:
        filename = os.path.basename(file)
        file_size = os.path.getsize(file)
        checksum = md5_checksum(file)
        compaund_key = File_object(filename, file_size, checksum)
        records[compaund_key].append(file)
    duplicates = {k: v for k, v in records.items() if len(v) > 1}
    return duplicates
  

def output_results(dict_of_duplicates):
    for file in dict_of_duplicates:
        print('Filename:', file.name, '/ size', file.size, 'bytes', '/ checksum', file.checksum)
        print('-' * 50)
        for path in dict_of_duplicates[file]:
            print(path)
        print('-' * 50,'\n')


if __name__ == '__main__':
    path_collection = enumerate_path()
    dupes = get_duplicates(path_collection)
    output_results(dupes)
    
"""
    if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
        filepath = sys.argv[1]
        dict_of_path = walk(filepath)
        print_duplicates(dict_of_path)
    else:
        print("Path not found.")
        print("Example launch: python duplicates.py <path>")
    """