from dataclasses import dataclass


@dataclass
class Ip:
    ip: str
    checked: bool


ip_range = [Ip("10.0.0.1", False), Ip("10.0.0.2", False), Ip("10.0.0.3", False), Ip("10.0.0.4", False),
           Ip("10.0.0.5", False), Ip("10.0.0.6", False)]

