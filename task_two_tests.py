import unittest

from task_two import find_last_scanned_ip, Ip


class TestTaskTwo(unittest.TestCase):
    def test_find_last_scanned_ip_6_ips(self):
        ip_range = [Ip("10.0.0.1", False), Ip("10.0.0.2", False), Ip("10.0.0.3", False), Ip("10.0.0.4", False),
                    Ip("10.0.0.5", False), Ip("10.0.0.6", False)]
        self.assertEqual("10.0.0.5", find_last_scanned_ip(ip_range))

    def test_find_last_scanned_ip_5_ips(self):
        ip_range = [Ip("10.0.0.1", False), Ip("10.0.0.2", False), Ip("10.0.0.3", False), Ip("10.0.0.4", False),
                    Ip("10.0.0.5", False)]
        self.assertEqual("10.0.0.3", find_last_scanned_ip(ip_range))

    def test_find_last_scanned_ip_4_ips(self):
        ip_range = [Ip("10.0.0.1", False), Ip("10.0.0.2", False), Ip("10.0.0.3", False), Ip("10.0.0.4", False)]
        self.assertEqual("10.0.0.1", find_last_scanned_ip(ip_range))

    def test_find_last_scanned_ip_3_ips(self):
        ip_range = [Ip("10.0.0.1", False), Ip("10.0.0.2", False), Ip("10.0.0.3", False)]
        self.assertEqual("10.0.0.3", find_last_scanned_ip(ip_range))

    def test_find_last_scanned_ip_2_ips(self):
        ip_range = [Ip("10.0.0.1", False), Ip("10.0.0.2", False)]
        self.assertEqual("10.0.0.1", find_last_scanned_ip(ip_range))


if __name__ == '__main__':
    unittest.main()
