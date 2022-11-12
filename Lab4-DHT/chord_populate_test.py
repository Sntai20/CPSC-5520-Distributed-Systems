import unittest
import os
import chord_populate

class TestChordPopulateMethods(unittest.TestCase):

    def test_find_file(self):
        # Arrange
        cp = chord_populate.ChordPopulate()
        filename = 'Career_Stats_Passing.csv'
        expected_file_path = f"{os.path.dirname(__file__)}/{os.path.basename(filename)}"

        # Act
        absolute_file_path = cp.find_file()

        # Assert
        self.assertTrue(expected_file_path == absolute_file_path)

    def test_read_file(self):
        # Arrange
        chord_populate_implementation = chord_populate.ChordPopulate()
        key = '9c92a752712a0c71bab443917237bd97009fb27f'
        steveramsey_dictionary = chord_populate_implementation.node_data_set_dictionary[key]

        # Act
        first_value = 'steveramsey/2523725'
        second_value = steveramsey_dictionary['Player Id']

        # error message in case if test case got failed
        message = "First value and second value are not equal !"

        # Assert
        # assertEqual() to check equality of first & second value
        self.assertEqual(first_value, second_value, message)

if __name__ == '__main__':
    unittest.main()
