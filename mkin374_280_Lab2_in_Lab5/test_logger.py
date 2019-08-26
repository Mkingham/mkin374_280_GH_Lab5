import unittest     # Import the Python unit testing framework
import logger # Our code to test


class LoggerTest(unittest.TestCase):
    ''' Unit tests for our logger functions. '''
    
    # Class used as the target passed into the logger program
    class targ(object):
        
         def targ(self, text):
            self.result = text
    
    def test_info(self):
        ''' Tests the info method in the Logger class'''
         
        # Arrange
        targetObj = LoggerTest.targ()
        logObj = logger.Logger(targetObj.targ)
        
        # Act
        logObj.info('This is a test!')
        
        # Assert
        assert(targetObj.result == '[INFO] This is a test!')
       
    def test_error(self):
        ''' Tests the info method in the Logger class'''
         
        # Arrange
        targetObj = LoggerTest.targ()
        logObj = logger.Logger(targetObj.targ)
        
        # Act
        logObj.error('This is a test!')
        
        # Assert
        assert(targetObj.result == '[WARNING] This is a test!')
        
# This allows running the unit tests from the command line (python test_logger.py)
if __name__ == '__main__':
    unittest.main()
