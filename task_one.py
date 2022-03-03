import csv
import os


def read_file(path):
    """Function that reads either a .txt file or a .csv file. It returns a list with all the rows in the
    files. For the .csv files it only returns the ip address to the list."""
    rows = []
    with open(path, 'r') as file:
        if path.endswith('.csv'):
            reader = csv.reader(file)

            for row in reader:
                # Adds only the ip address (last item on the row) to the list.
                rows.append(row[-1])
            return rows
        elif path.endswith('.txt'):
            return [line.replace("\n", "") for line in file.readlines()]


def get_all_files_in_folder(path):
    """Gets a list of files in a given folder."""
    return os.listdir(path)


def compare_ips_in_lists(list_to_compare, list_to_be_compared):
    """Compares two lists and returns the index of where a match occurs."""
    for ip_to_compare in list_to_compare:
        for ip_to_be_compared in list_to_be_compared:
            if ip_to_compare == ip_to_be_compared:
                return list_to_be_compared.index(ip_to_be_compared)
    return None


def find_txt_file(files):
    """Finds a txt file in a list of files."""
    for file in files:
        if file.endswith('.txt'):
            return file
    return None


def compare_ips_in_files(path):
    """Takes in a folder path containing csv file(s) and a txt file. It does then compare every csv file with
    the txt file. It then returns a string with the file name and line of the first match."""
    files = get_all_files_in_folder(path)

    txt_file = find_txt_file(files)

    files.remove(txt_file)
    txt_file = read_file(path + '/' + txt_file)

    for csv_file in files:
        line = compare_ips_in_lists(txt_file, read_file(path + '/' + csv_file))

        if line is not None:
            return "Found match in csv file: " + csv_file + " on line: " + str(line + 1)
    return "No matches found."
