import csv
import os

file_directory = os.path.join('analysis','election_analysis.txt')

#using the open() function with the 'w' mode we will write data to the file.
open(file_directory, 'w')