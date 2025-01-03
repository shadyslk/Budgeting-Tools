from tabula import read_pdf
from sys import argv

#get the file from argument if provided

file = argv[1]
print(f'Reading from "{file}"...')

#parse through file for a table and save it as a dataframe

tables = read_pdf(file, pages="all")
print(tables)

#put dataframe into an excel file