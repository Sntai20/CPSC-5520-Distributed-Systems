"""
STUDENT: Antonio Santana
FILE: chord_populate.py

DESCRIPTION:
    This program demonstrates populates data from CSV file into network of nodes correctly.
    Support adding a new data value to the network, given (key, value) via any active node.
    Add must be efficient, make use of predecessor, successor, and finger tables as 
    appropriate using key SHA1 hash and recursive RPC.

    chord_populate takes a port number of an existing node and the filename of the data file.

USAGE:
    python3 chord_populate.py

REFERENCES:
    Read a csv file. https://docs.python.org/3/library/csv.html

"""

import csv
import os

class ChordPopulate:
    "Methods to interface with the data."
    def __init__(self):
        self.absolute_file_path = self.find_file()
        self.read_file()

    def find_file(self):
        """
        Find the files.
        Filename: Career_Stats_Passing.csv
        File path: ./Lab4-DHT/Career_Stats_Passing.csv
        Relative path: ~./repo/CPSC-5520-Distributed-Systems/Lab4-DHT/Career_Stats_Passing.csv
        """
        print(f'Current Working Directory: {os.getcwd()}')
        filename = 'Career_Stats_Passing.csv'
        absolute_file_path = f"{os.path.dirname(__file__)}/{os.path.basename(filename)}"
        print('File name :    ', os.path.basename(filename))
        print('Directory Name:     ', os.path.dirname(__file__))
        print(f"Absolute path of the {filename}:     {absolute_file_path}")
        return absolute_file_path

    def read_file(self):
        """
        Reads a file.
        """
        with open(f"{self.absolute_file_path}", newline='', encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(', '.join(row))

if __name__ == '__main__':
    # Clearing the Screen
    os.system('clear')

    chord_populate = ChordPopulate()
