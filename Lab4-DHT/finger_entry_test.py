import unittest
import chord_node

class TestFingerEntryMethods(unittest.TestCase):

    def test_FingerEntry_default_constructor(self):
        # Arrange
        # Port number of an existing node (or 0 to indicate 
        # it should start a new network)
        new_network = 0
        node_number = 1
        finger_entry = chord_node.FingerEntry(new_network, node_number)

        # Act
        first_value = node_number
        finger_entry.node = node_number
        second_value = finger_entry.node

        # error message in case if test case got failed
        message = "First value and second value are not equal !"

        # Assert
        # assertEqual() to check equality of first & second value
        self.assertEqual(first_value, second_value, message)

if __name__ == '__main__':
    unittest.main()
