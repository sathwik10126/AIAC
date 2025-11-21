import unittest
import copy
import task_1

class TestRideSort(unittest.TestCase):
    def test_merge_sort_empty(self):
        arr = []
        result = task_1.merge_sort(arr)
        self.assertEqual(result, [])

    def test_merge_sort_single(self):
        arr = [5]
        result = task_1.merge_sort(arr)
        self.assertEqual(result, [5])

    def test_merge_sort_general(self):
        arr = [12, 5, 7, 3, 18]
        expected = sorted(arr)
        self.assertEqual(task_1.merge_sort(arr), expected)

    def test_quick_sort_empty(self):
        arr = []
        result = task_1.quick_sort(arr)
        self.assertEqual(result, [])

    def test_quick_sort_single(self):
        arr = [5]
        result = task_1.quick_sort(arr)
        self.assertEqual(result, [5])

    def test_quick_sort_general(self):
        arr = [25, 10, 40, 8, 15, 2]
        expected = sorted(arr)
        self.assertEqual(task_1.quick_sort(arr), expected)

    def test_both_sorts_same_result(self):
        cases = [
            [],
            [1],
            [3, 1, 2],
            [6, 6, 3, 9, 1, 1, 8],
            [5, -1, 0, 5, 2]
        ]
        for arr in cases:
            with self.subTest(arr=arr):
                a = copy.copy(arr)
                b = copy.copy(arr)
                self.assertEqual(task_1.merge_sort(a), task_1.quick_sort(b))

    def test_sort_etas_merge(self):
        arr = [12, 5, 7, 3, 18]
        sorted_etas = task_1.sort_etas(arr, algorithm='merge')
        self.assertEqual(sorted_etas, sorted(arr))

    def test_sort_etas_quick(self):
        arr = [25, 10, 40, 8, 15, 2]
        sorted_etas = task_1.sort_etas(arr, algorithm='quick')
        self.assertEqual(sorted_etas, sorted(arr))

    def test_sort_etas_does_not_mutate_input(self):
        arr = [6, 6, 3, 9, 1, 1, 8]
        original = copy.copy(arr)
        _ = task_1.sort_etas(arr, algorithm='merge')
        self.assertEqual(arr, original)
        _ = task_1.sort_etas(arr, algorithm='quick')
        self.assertEqual(arr, original)

if __name__ == '__main__':
    unittest.main()
