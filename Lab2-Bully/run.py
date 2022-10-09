"""Simple program to run this lab."""
import os
import time

print("python3 gcd2.py 23633")
os.system('python3 gcd2.py >> log-gcd2.txt &')

print("Wait 0.5 seconds")
time.sleep(1)

print("python3 lab2.py localhost 23633 2022-12-01 1234567")
os.system('python3 lab2.py localhost 23633 2022-12-01 1234567')

os.system("nohup python3 gcd2.py > log-gcd2.txt")
