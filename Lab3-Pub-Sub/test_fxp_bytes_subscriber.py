import unittest
import fxp_bytes_subscriber

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    # Figure this out later if we need to.
    # def test_marshall(self):
    #     incoming_data = "b'\x00\x05\xeb\xe1_|\xd9HUSDCHF\xa1J\xcd\x1eh\x05\xf0?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\xeb\xe1_|\xd9HAUDUSD\x05\xc0x\x06\r\xfd\xe7?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\xeb\xe1_|\xd9HUSDJPYj\xdeq\x8a\x8e\xf8X@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\xeb\xe1_|\xd9HGBPUSD\xfbWV\x9a\x94\x02\xf4?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\xeb\xe1_|\xd9HEURUSD\xa5\xa0\xdbK\x1a\xa3\xf1?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\xeb\xe1_|\xd9HAUDCAD\xb8{\x8c\x1ci>\xd8?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\xeb\xe1_|\xd9HCADCHF\xb8{\x8c\x1ci>\xf8?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'"
    #     # Parse the individual quotes from the message.
    #     message = fxp_bytes_subscriber.unmarshall_message(incoming_data)

if __name__ == '__main__':
    unittest.main()
