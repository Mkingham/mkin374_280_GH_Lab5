import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class TestFactorial(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_factorial(self):
        ''' Tests the add function. '''
        # Arrange
        number = 2
        
        # Act
        result = maths.factorial(number)
        
        # Assert
        self.assertEqual(result, 2)

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
