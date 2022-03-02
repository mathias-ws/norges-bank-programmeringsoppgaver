from dataclasses import dataclass


@dataclass
class Ip:
    ip: str
    checked: bool


ip_range = [Ip("10.0.0.1", False), Ip("10.0.0.2", False), Ip("10.0.0.3", False), Ip("10.0.0.4", False),
            Ip("10.0.0.5", False), Ip("10.0.0.6", False)]

flag = True

i = 0
counter = 0
while flag:
    ting = True

    i = (i + 1) % len(ip_range)
    if not ip_range[i].checked:
        ip_range[i].checked = True
        counter += 1

        if counter == len(ip_range):
            print(ip_range[i].ip)
            flag = False
    else:
        ting = False

    if ting:
        i = (i + 1) % len(ip_range)
