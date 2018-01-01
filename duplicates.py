import os
import sys
from collections import defaultdict, namedtuple


File_info = namedtuple('File', 'name size')


def get_path_to_files(path):
    path_to_files_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file_name in filenames:
            full_path = os.path.join(dirpath, file_name)
            path_to_files_list.append(full_path)
    return path_to_files_list


def get_duplicate_files(path_to_files_list):
    path_to_files_dict = defaultdict(list)
    for path in path_to_files_list:
        file_name = os.path.basename(path)
        file_size = os.path.getsize(path)
        file_info = File_info(file_name, file_size)
        path_to_files_dict[file_info].append(path)
    duplicate_files = {
        file: file_paths
        for file, file_paths
        in path_to_files_dict.items()
        if len(file_paths) > 1
    }
    return duplicate_files


def print_results_to_stdout(duplicate_files_dict):
    separation_line = '-' * 50
    for duplicate_file in duplicate_files_dict:
        print('Filename:', duplicate_file.name, '/ size',
              duplicate_file.size, 'bytes')
        print(separation_line)
        for path in duplicate_files_dict[duplicate_file]:
            print(path)
        print(separation_line, '\n')


def main():
    if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
        path = sys.argv[1]
        path_to_files_list = get_path_to_files(path)
        duplicate_files = get_duplicate_files(path_to_files_list)
        if len(duplicate_files) > 0:
            print_results_to_stdout(duplicate_files)
        else:
            print('Duplicates not found')
    else:
        print('Path not found.')
        print('Example launch: python duplicates.py <path>')


if __name__ == '__main__':
    main()
