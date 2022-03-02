from dataclasses import dataclass


# Class used to define an ip object.
@dataclass
class Ip:
    ip: str
    checked: bool


# Function inspired by: https://tkit.dev/2011/09/11/how-to-generate-an-ip-range-list-in-python/
# Function that takes in a start and an end ip and generates a list of the ips in the range.
def generate_ip_range(start_ip, end_ip):
    ip_range = []

    # Casting to ints is inspired by: https://stackoverflow.com/a/5306094
    first_ip = [int(octet) for octet in (start_ip.split("."))]
    last_ip = [int(octet) for octet in (end_ip.split("."))]

    temp_ip = first_ip

    ip_range.append(Ip(start_ip, False))

    while temp_ip != last_ip:
        first_ip[3] += 1

        # Counts up every octet.
        for i in (3, 2, 1):
            if temp_ip[i] == 256:
                temp_ip[i] = 0
                temp_ip[i - 1] += 1

        ip_range.append(Ip(".".join(map(str, temp_ip)), False))

    return ip_range


# Function that finds the last scanned ip according to the specifications.
def find_last_scanned_ip(ip_list):
    i = 0
    counter = 0

    while True:
        i = (i + 1) % len(ip_list)

        # Checks that the ip is not already checked.
        if not ip_list[i].checked:
            ip_list[i].checked = True
            counter += 1

            # Checks if the algorithm is done.
            if counter == len(ip_list):
                return ip_list[i].ip

            # Counting up the index to skip the already checked ips.
            while ip_list[((i + 1) % len(ip_list))].checked:
                i = (i + 1) % len(ip_list)

            i = (i + 1) % len(ip_list)
