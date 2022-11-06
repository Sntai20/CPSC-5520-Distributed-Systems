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
        cp = chord_populate.ChordPopulate()

        # Act
        something_to_store_the_file_contents = cp.read_file()

        # Assert
        self.assertTrue(something_to_store_the_file_contents)

if __name__ == '__main__':
    unittest.main()
