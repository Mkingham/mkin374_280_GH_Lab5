import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        # Arrange
        numbers = [10,5,0.5,0.4,-1,2,-10,-18, 7, 2.9 ]
        answers = [15,0.9,1,-28, 9.9]
        count = 0
        
        # Loops through and tests the add function on different types of numbers. Act/Assert steps
        for i in range(len(numbers), 2):
            sum = maths.add(numbers[i], numbers[i+1])
            self.assertEqual(sum, answers[count])
            count += 1
            
        # Tests the add function with the addition of the new parameter
        # Arrange
        numbers = [3,7,15,5,21,29]
        answersb15 = ['A', '15', '35']
        count = 0
        
        # Act, Assert. Tests add function with base 15 conversion
        for i in range(len(numbers), 2):
            sum = maths.add(numbers[i], numbers[i+1], 15)
            self.assertEqual(sum, answers[count])
            count += 1
        

        
    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        fib5 = maths.fibonacci(5)
        self.assertEqual(fib5, 5)
        
        
    def test_convert_base(self):
        '''Tests the convert_base function. '''
        # Tests converting to base 15, and base 2
        # Arrange
        numbers = [10,20,50,100,500]
        resultsb15 = ['A', '15', '35', '6A', '235']
        resultsb2 = ['1010', '10100', '110010', '1100100', '111110100']
        
        # Action, and Assert
        for i in range(len(numbers)):
            base15num = maths.convert_base(numbers[i], 15)
            base2num = maths.convert_base(numbers[i], 2)
            self.assertEqual(base15num, resultsb15[i])
            self.assertEqual(base2num, resultsb2[i])
        


# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
