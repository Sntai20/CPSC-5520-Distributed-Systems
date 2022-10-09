"""Simple program to run this lab."""
import os
import time

# Clearing the Screen
os.system('clear')

print("\nStart of gcd2\n")
print("python3 Lab2-Bully/gcd2.py 23633")
os.system('python3 Lab2-Bully/gcd2.py >> log-gcd2.txt &')

print("Wait 0.25 seconds for the server to start listening")
time.sleep(0.25)
print("\nEnd of gcd2")

print("\n\n\nStart of Members\n")
print("python3 Lab2-Bully/member1.py localhost 23633 2022-11-01 1234561")
os.system('python3 Lab2-Bully/member1.py localhost 23633 2022-11-01 1234561')
print("\n\n")
print("python3 Lab2-Bully/member2.py localhost 23633 2022-12-01 1234568")
os.system('python3 Lab2-Bully/member2.py localhost 23633 2022-12-01 1234568')
print("\n\nEnd of Members")

print("\n\n\nStart of lab2\n")
print("python3 Lab2-Bully/lab2.py localhost 23633 2022-11-01 1234567")
os.system('python3 Lab2-Bully/lab2.py localhost 23633 2022-11-01 1234567')
print("\n\n\nEnd of lab2\n\n\n")

print("Shutting down the gcd2 server.")
os.system("nohup python3 Lab2-Bully/gcd2.py > log-gcd2.txt")
os.system("kill $(lsof -i:23633)")
