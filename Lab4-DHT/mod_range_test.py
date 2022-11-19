import unittest
import chord_node

class TestModRangeMethods(unittest.TestCase):

    def test_ModRange_default_constructor(self):
        # Arrange
        # Port number of an existing node (or 0 to indicate 
        # it should start a new network)
        start = 0
        stop = 4
        divisor = 100
        finger_entry = chord_node.ModRange(start, stop, divisor)

        # Act
        first_value = stop
        finger_entry.node = stop
        second_value = finger_entry.node

        # error message in case if test case got failed
        message = "First value and second value are not equal !"

        # Assert
        # assertEqual() to check equality of first & second value
        self.assertEqual(first_value, second_value, message)

if __name__ == '__main__':
    unittest.main()
