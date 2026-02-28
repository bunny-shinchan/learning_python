from pathlib import Path

#Absolute path
# c:\Porgram File\Microsft
#  /usr/local/bin
#Relative Path

path = Path()
for file in (path.glob('*.py')):
    print(file)
    #directory.py

#****************************************
#glob - with this method we can search for files and directory in the current path.
# * - all files and directories
# | - search pattern
# *.* - extension
# *.xls - to find all the excel files, *.py to find all the python files in the directory.
#****************************************

