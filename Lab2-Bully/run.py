"""
CPSC 5520, Seattle University
This is free and unencumbered software released into the public domain.
:Authors: Antonio Santana
:Version: 000-01

Simple program to run this lab.
"""

# from Lab2-Bully.lab2 import Lab2
import os
import time

def run():
    """Simple program to run this lab."""

    # Clearing the Screen
    os.system('clear')

    print("\nStart of gcd2\n")
    print("python3 Lab2-Bully/tests/gcd2.py 23633")
    os.system('python3 Lab2-Bully/tests/gcd2.py >> log-gcd2.txt &')

    print("Wait 0.25 seconds for the server to start listening")
    time.sleep(0.25)
    print("\nEnd of gcd2")

    print("\n\n\nStart of Members\n")
    print("python3 Lab2-Bully/tests/member1.py localhost 23633 2022-11-01 1234561")
    os.system('python3 Lab2-Bully/tests/member1.py localhost 23633 2022-11-01 1234561')
    print("\n\n")
    print("python3 Lab2-Bully/tests/member2.py localhost 23633 2022-12-01 1234568")
    os.system('python3 Lab2-Bully/tests/member2.py localhost 23633 2022-12-01 1234568')
    # print("\n\n")
    # print("python3 Lab2-Bully/member3.py localhost 23633 2022-11-05 1234566")
    # os.system('python3 Lab2-Bully/member3.py localhost 23633 2022-11-05 1234566')
    print("\n\nEnd of Members")

    # print("\n\n\nStart of lab2\n")
    # print("python3 Lab2-Bully/lab2.py localhost 23633 2022-11-01 1234567")
    # os.system('python3 Lab2-Bully/lab2.py localhost 23633 2022-11-01 1234567')
    # print("\n\n\nEnd of lab2\n\n\n")

    print("\n\n\nStart of lab2solution\n")
    print("python3 Lab2-Bully/lab2solution.py localhost 23633 1234567 2022-11-01")
    os.system('python3 Lab2-Bully/lab2solution.py localhost 23633 1234567 2022-11-01')
    print("\n\n\nEnd of lab2solution\n\n\n")

    print("Shutting down the gcd2 server.")
    os.system("nohup python3 Lab2-Bully/tests/gcd2.py > tests/log-gcd2.txt")
    # os.system("kill $(lsof -i:23633)")

if __name__ == '__main__':
    run()
