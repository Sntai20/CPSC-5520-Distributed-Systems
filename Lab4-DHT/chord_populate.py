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
import hashlib
import os

class ChordPopulate:
    "Methods to interface with the data."
    def __init__(self):
        Career_Stats_Dictionary = dict()
        self.absolute_file_path = self.find_file()
        Career_Stats_Dictionary = self.read_file()

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
        Reads a file with the following fieldnames in the first row:
        Player Id,Name,Position,Year,Team,Games Played,Passes Attempted,Passes Completed,
        Completion Percentage,Pass Attempts Per Game,Passing Yards,Passing Yards Per Attempt,
        Passing Yards Per Game,TD Passes,Percentage of TDs per Attempts,Ints,Int Rate,
        Longest Pass,Passes Longer than 20 Yards,Passes Longer than 40 Yards,Sacks,
        Sacked Yards Lost,Passer Rating

        Create an object that operates like a regular reader but maps the information
        in each row to a dict whose keys are given by the optional fieldnames parameter.
        """
        with open(f"{self.absolute_file_path}", newline='', encoding='utf-8') as csvfile:
            # reader = csv.DictReader(csvfile, delimiter=' ', quotechar='|')
            #reader = csv.DictReader(csvfile)
            return csv.DictReader(csvfile)
            # print(reader.fieldnames)
            # for row in reader:
                # print(row['Player Id'], row['Year'])
                # this one self.hash_something(row['Player Id'], row['Year'])
                #player_id = row['Player Id']
                #year = row['Year']
                #key = hashlib.sha1()
                #key.update(f'{player_id}'.encode('ASCII'))
                #key.update(f'{year}'.encode('ASCII'))
                #key.hexdigest()
                #player_id_year = (player_id + year)
                #print(f"Sha1 Hash {key.hexdigest()} = Player Id + Year {player_id_year}")

    def hash_something(self, player_id, year):
        """
        Treat the value in the first column (playerid) concatenated
        with the fourth column (year) as the key and use SHA-1 to hash it.
        """
        key = hashlib.sha1()
        key.update(f'{player_id}'.encode('ASCII'))
        key.update(f'{year}'.encode('ASCII'))
        key.hexdigest()
        player_id_year = (player_id + year)
        print(f"Sha1 Hash {key.hexdigest()} = Player Id + Year {player_id_year}")

if __name__ == '__main__':
    # Clearing the Screen
    os.system('clear')

    chord_populate = ChordPopulate()
