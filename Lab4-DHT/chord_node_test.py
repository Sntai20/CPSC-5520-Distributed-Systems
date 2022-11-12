import unittest
import chord_node

class TestChordNodeMethods(unittest.TestCase):

    def test_find_predecessor(self):
        # Arrange
        # Port number of an existing node (or 0 to indicate 
        # it should start a new network)
        new_network = 0
        node = chord_node.ChordNode(new_network)

        # Act
        first_value = None
        second_value = node.find_predecessor(first_value)

        # error message in case if test case got failed
        message = "First value and second value are not equal !"

        # Assert
        # assertEqual() to check equality of first & second value
        self.assertEqual(first_value, second_value, message)

    # def test_read_file(self):
    #     # Arrange
    #     chord_populate_implementation = chord_populate.ChordPopulate()
    #     key = 'd55607515a6c96f2ff50b87a62d26e5ce18e2e07'
    #     steveramsey_dictionary = chord_populate_implementation.node_data_set_dictionary[key]

    #     # Act
    #     first_value = 'steveramsey/2523725'
    #     second_value = steveramsey_dictionary['Player Id']

    #     # error message in case if test case got failed
    #     message = "First value and second value are not equal !"

    #     # Assert
    #     # assertEqual() to check equality of first & second value
    #     self.assertEqual(first_value, second_value, message)

if __name__ == '__main__':
    unittest.main()
