"""
CPSC 5520, Seattle University
This is free and unencumbered software released into the public domain.
:Authors: Antonio Santana
:Version: 000-01

Simple program to run this lab.
"""

import os
import time

def run():
    """Simple program to run this lab."""

    # Clearing the Screen
    os.system('clear')

    # Run the subscriber first.
    filename = "subscriber"
    print(f"\n\n\nStart of {filename}\n")
    print(f"python3 Lab3-Pub-Sub/{filename}.py >> log-{filename}.txt &")
    os.system(f'python3 Lab3-Pub-Sub/{filename}.py')
    print(f"\n\n\nEnd of {filename}\n\n\n")

    filename = "publisher"
    print(f"\n\n\nStart of {filename}\n")
    print(f"python3 Lab3-Pub-Sub/{filename}.py")
    os.system(f'python3 Lab3-Pub-Sub/{filename}.py')
    print(f"\n\n\nEnd of {filename}\n\n\n")

    # print("\n\n\nStart of lab3\n")
    # print("python3 Lab3-Pub-Sub/lab3.py")
    # os.system('python3 Lab3-Pub-Sub/lab3.py')
    # print("\n\n\nEnd of lab3\n\n\n")

if __name__ == '__main__':
    run()
