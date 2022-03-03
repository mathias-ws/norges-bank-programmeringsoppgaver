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
    return os.listdir(path)


print(get_all_files_in_folder(r'task_one_example_data_set'))
print(read_file(r'task_one_example_data_set/ips2.csv'))
