import unittest
from unittest.mock import *
from clustering import cluster_data


class TestClusterAlgo(unittest.TestCase):
    def setUp(self):
        self.data = [[1, 2], [3, 4], [5, 6]]

    def test_run_cluster_algo(self):
        result = cluster_data(self.data)
        self.assertEqual(len(result), len(self.data))


if __name__ == "__main__":
    unittest.main()
