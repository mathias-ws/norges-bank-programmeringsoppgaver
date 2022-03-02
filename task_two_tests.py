import unittest

from task_two import find_last_scanned_ip, Ip, generate_ip_range


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

    def test_generate_10_ips(self):
        ip_range = generate_ip_range("10.0.0.1", "10.0.0.10")
        self.assertEqual(10, len(ip_range))

    def test_generate_200_ips(self):
        ip_range = generate_ip_range("10.0.0.1", "10.0.0.200")
        self.assertEqual(200, len(ip_range))

    def test_generate_ips_and_verify_the_correctness_of_fourth_octet(self):
        ip_range = generate_ip_range("10.0.0.254", "10.0.1.2")
        self.assertEqual(
            [Ip("10.0.0.254", False), Ip("10.0.0.255", False), Ip("10.0.1.0", False), Ip("10.0.1.1", False),
             Ip("10.0.1.2", False)], ip_range)

    def test_generate_ips_and_verify_the_correctness_of_third_octet(self):
        ip_range = generate_ip_range("10.0.254.254", "10.0.255.2")
        self.assertEqual(
            [Ip("10.0.254.254", False), Ip("10.0.254.255", False), Ip("10.0.255.0", False), Ip("10.0.255.1", False),
             Ip("10.0.255.2", False)], ip_range)

    def test_generate_ips_and_verify_the_correctness_of_second_octet(self):
        ip_range = generate_ip_range("10.254.255.255", "10.255.255.254")
        self.assertEqual(65536, len(ip_range))


if __name__ == '__main__':
    unittest.main()
