# import unittest and longerString
import unittest
import longerString


# create testCases
class TestLongerString(unittest.TestCase):
    # testing output type
    def test_outputType(self):
        output = longerString.longString('quil', 'dennis')
        self.assertIsInstance(output, str)  # tests whether type of output is a string

    # another test for longest output length
    def test_outPutLength(self):
        testString = longerString.longString('mesier', 'hubbles')
        self.assertEqual(len(testString),len('hubbles'))

    # another test for equal length strings
    def test_equalOutput(self):
        testEqual = longerString.longString('mufasa', 'dennis')
        newTestEqual = testEqual.split('\n')
        self.assertEqual(len(newTestEqual[0]), len(newTestEqual[1]))


# running the testcases
if __name__ == '__main__':
    unittest.main()