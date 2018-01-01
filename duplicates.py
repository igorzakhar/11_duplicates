import os
import sys
import hashlib
from collections import defaultdict, namedtuple


File_object = namedtuple('File', 'name size checksum')


def md5_checksum(path_to_file, blocksize=65536):
    checksum = hashlib.md5()
    with open(path_to_file, 'rb') as fp:
        buffer = fp.read(blocksize)
        while len(buffer) > 0:
            checksum.update(buffer)
            buffer = fp.read(blocksize)
    return checksum.hexdigest()


def get_path_to_files(path):
    path_to_files_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file_name in filenames:
            fulpath = os.path.join(dirpath, file_name)
            path_to_files_list.append(fulpath)
    return path_to_files_list


def get_duplicates(path_to_files_list):
    duplicate_files_dict = defaultdict(list)
    for path in path_to_files_list:
        file_name = os.path.basename(path)
        file_size = os.path.getsize(path)
        checksum = md5_checksum(path)
        compaund_key = File_object(file_name, file_size, checksum)
        duplicate_files_dict[compaund_key].append(path)
    duplicates = {key: value
                  for key, value
                  in duplicate_files_dict.items()
                  if len(value) > 1}
    return duplicates


def print_results_to_stdout(dict_of_duplicates):
    for duplicate_file in dict_of_duplicates:
        print('Filename:', duplicate_file.name,
              '/ size', duplicate_file.size, 'bytes',
              '/ checksum', duplicate_file.checksum)
        print('-' * 50)
        for path in dict_of_duplicates[duplicate_file]:
            print(path)
        print('-' * 50, '\n')


def main():
    if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
        path = sys.argv[1]
        path_to_files_list = get_path_to_files(path)
        duplicate_files = get_duplicates(path_to_files_list)
        print_results_to_stdout(duplicate_files)
    else:
        print("Path not found.")
        print("Example launch: python duplicates.py <path>")


if __name__ == '__main__':
    main()
