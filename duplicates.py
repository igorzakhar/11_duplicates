import os
import sys
from collections import defaultdict, namedtuple


File_attr = namedtuple('File', 'name size')


def get_path_to_files(path):
    path_to_files_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file_name in filenames:
            fulpath = os.path.join(dirpath, file_name)
            path_to_files_list.append(fulpath)
    return path_to_files_list


def get_duplicates(path_to_files_list):
    path_to_files_dict = defaultdict(list)
    for path in path_to_files_list:
        file_name = os.path.basename(path)
        file_size = os.path.getsize(path)
        compaund_key = File_attr(file_name, file_size)
        path_to_files_dict[compaund_key].append(path)
    duplicates = {file: file_paths
                  for file, file_paths
                  in path_to_files_dict.items()
                  if len(file_paths) > 1}
    return duplicates


def print_results_to_stdout(dict_of_duplicates):
    separation_line_length = 50
    for duplicate_file in dict_of_duplicates:
        print('Filename:', duplicate_file.name,
              '/ size', duplicate_file.size, 'bytes')
        print('-' * separation_line_length)
        for path in dict_of_duplicates[duplicate_file]:
            print(path)
        print('-' * separation_line_length, '\n')


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
