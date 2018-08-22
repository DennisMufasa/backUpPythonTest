# import unittest & passwordChecker
import unittest
import passwordChecker



# create testCases
class TestPasswords(unittest.TestCase):
    # test output type
    def test_OutPutType(self):
        # output = passwordChecker.passCheck("stRand@4")
        output = self.dataGenerator()
        self.assertIsInstance(output, str)

# another test. Check if strings returned dont exceed 12 chars
    def test_maxLength(self):
        # output = passwordChecker.passCheck('rgHjd4', 'lks@PL56jl', 'Amg@85Lolo#Sdu')
        output = self.dataGenerator()
        newOutput = output.split(', ')
        # self.assertLessEqual(len(newOutput[2]), 12)
        for i in newOutput:
            self.assertTrue(len(i) < 12)

# another test. Check whether the string returned isnt less than 6 char long
    def test_minLength(self):
        # output = passwordChecker.passCheck('rA@4', 'dennY@50')
        output = self.dataGenerator()
        newOutput = output.split(', ')
        for i in newOutput:
            self.assertTrue(len(i) > 5)

    #     another test checking for A-Z
    def test_upperCase(self):
        # output = passwordChecker.passCheck('asd@wer', 'Ae#jkWh')
        output = self.dataGenerator()
        newOutput = output.split(', ')
        for i in newOutput:
            self.assertRegex(i, r'[A-Z]')


#     another test checking for a-z
    def test_LowerCase(self):
        # output = passwordChecker.passCheck('ASD@#KL', 'Ae#jkWh')
        output = self.dataGenerator()
        newOutput = output.split(', ')
        for i in newOutput:
            self.assertRegex(i, r'[a-z]')


# another test checking for 0-9
    def test_numbers(self):
        # output = passwordChecker.passCheck('AeS4efk', 'Ae#jkWh')
        output = self.dataGenerator()
        newOutput = output.split(', ')
        for i in newOutput:
            self.assertRegex(i, r'[0-9]')


# another test checking for $#@
    def test_specialChars(self):
        output = self.dataGenerator()
        newOutput = output.split(', ')
        for i in newOutput:
            self.assertRegex(i, r'[$#@]')


# a function used to pass data to the above functions
    def dataGenerator(self):
        output = passwordChecker.passCheck('a7d@w','WErty4hjk@sdhj#','as@r12ggt','ASF7#45','asA78lK52','aS7#dF8@','sDfr#45')
        return output

# running the tests
if __name__ == '__main__':
    unittest.main()
