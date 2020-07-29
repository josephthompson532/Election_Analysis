#Add our Dependencies
import csv
import os

file_to_save = os.path.join('analysis', 'election_analysis.txt')

with open(file_to_save, 'w') as myfile:

    
    myfile.write("Counties in the Election\n_______________________\n")
    myfile.write("Arapahoe\n")
    myfile.write("Denver\n")
    myfile.write("Jefferson")