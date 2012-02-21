#!/usr/bin/python
"""
Python exercise to sanitize data files
by replacing Sex: N with Sex: M
"""

# IMPORTS
import os

# CONSTANTS
DIR="cleaneddata"

# MAIN
if __name__ == "__main__":
	for DATFILE in os.listdir(DIR):
		F = open(DIR + "/" + DATFILE, "rw+")
		L = F.readlines()
		try:
			L[L.index("Sex: N\n")] = "Sex: M\n"
			F.seek(0)
			F.writelines(L)
			F.close()
		except ValueError:
			F.close()
