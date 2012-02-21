#!/usr/bin/python
"""
Python exercise to sanitize data files
by replacing Sex: N with Sex: M
"""

# IMPORTS
import os

# CONSTANTS
DATADIR="cleaneddata"

# FUNCTIONS
def find_data_files(DIR=DATADIR):
	return os.listdir(DIR)

def missing_gender(LINE):
	if "Sex: N" in LINE: return True
	return False

def fix_gender(FILE, LINE)
	# given FILE and LINE replace LINE with LINE(remove :N replace :M)
	return file	

# MAIN
if __name__ == "__main__":
	print "this is sanitize.py"
	# loop through and do the necessary
