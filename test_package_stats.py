import requests
import unittest
from package_stats import get_data, count_packages


class TestPackageStats(unittest.TestCase):
    def setUp(self):
        self.mirror_url = "http://ftp.uk.debian.org/debian/dists/stable/main"

    def test_invalid_url(self):
        arch = "invalid_arch"
        with self.assertRaises(requests.exceptions.RequestException):
            get_data(arch, self.mirror_url)

    def test_valid_url(self):
        arch = "arm64"
        data = get_data(arch, self.mirror_url)
        self.assertIsNotNone(data)

    def test_count_packages(self):
        arch = "arm64"
        list = count_packages(get_data(arch, self.mirror_url))
        self.assertTrue(list[0][1] > list[1][1])
        self.assertTrue(list[1][1] > list[2][1])
        self.assertTrue(list[2][1] > list[3][1])
        self.assertTrue(list[3][1] > list[4][1])
        self.assertTrue(list[4][1] > list[5][1])
        self.assertTrue(len(list) == 10)


if __name__ == "__main__":
    unittest.main()
