import unittest
from mean_var_calculator import calculate


class TestCalculate(unittest.TestCase):

    def test_correct_output(self):
        result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        expected = {
            'mean':               [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance':           [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max':                [[6, 7, 8], [2, 5, 8], 8],
            'min':                [[0, 1, 2], [0, 3, 6], 0],
            'sum':                [[9, 12, 15], [3, 12, 21], 36],
        }
        self.assertEqual(result, expected)

    def test_raises_on_short_list(self):
        with self.assertRaises(ValueError) as ctx:
            calculate([1, 2, 3])
        self.assertEqual(str(ctx.exception), "List must contain nine numbers.")

    def test_second_dataset(self):
        result = calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])
        self.assertEqual(result['mean'], [[11/3, 5.0, 3.0], [10/3, 4.0, 13/3], 35/9])
        self.assertEqual(result['max'], [[8, 6, 7], [6, 8, 7], 8])
        self.assertEqual(result['min'], [[1, 4, 0], [2, 0, 1], 0])
        self.assertEqual(result['sum'], [[11, 15, 9], [10, 12, 13], 35])


if __name__ == '__main__':
    unittest.main()
