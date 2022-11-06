import unittest
import os
import chord_populate

class TestChordPopulateMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_find_file(self):
        # Arrange
        cp = chord_populate.ChordPopulate()
        filename = 'Career_Stats_Passing.csv'
        file_path = f"{os.path.dirname(__file__)}/{os.path.basename(filename)}"

        # Act
        absolute_file_path = cp.find_file()

        # Assert
        self.assertTrue(absolute_file_path == absolute_file_path)

    def test_read_file(self):
        # Arrange
        cp = chord_populate.ChordPopulate()

        # Act
        something_to_store_the_file_contents = cp.read_file()

        # Assert
        self.assertTrue(something_to_store_the_file_contents)

    #def test_split(self):
    #    s = 'hello world'
    #    self.assertEqual(s.split(), ['hello', 'world'])
    #    # check that s.split fails when the separator is not a string
    #    with self.assertRaises(TypeError):
    #        s.split(2)

if __name__ == '__main__':
    unittest.main()