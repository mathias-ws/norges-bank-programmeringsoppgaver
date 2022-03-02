from dataclasses import dataclass


@dataclass
class Ip:
    ip: str
    checked: bool


ip_range = [Ip("10.0.0.1", False), Ip("10.0.0.2", False), Ip("10.0.0.3", False), Ip("10.0.0.4", False),
            Ip("10.0.0.5", False)]


def find_last_scanned_ip(ip_list):
    i = 0
    counter = 0

    while True:
        i = (i + 1) % len(ip_list)
        if not ip_list[i].checked:
            ip_list[i].checked = True
            counter += 1

            if counter == len(ip_list):
                return ip_list[i].ip

            while ip_list[((i + 1) % len(ip_list))].checked:
                i = (i + 1) % len(ip_list)

            i = (i + 1) % len(ip_list)


