# Write a python program to print the contents of a directory using the os module.
import os

directory = "."  # Current directory
for item in os.listdir(directory):
    print(item)