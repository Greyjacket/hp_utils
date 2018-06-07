import csv, sys, math, operator, re, os
from ftfy import fix_encoding, fix_text
import ftfy

try:
	filename = sys.argv[1]
except:
	print ("\nPlease input a valid CSV filename.\n")
	print ("Format: python scriptname filename.\n")
	exit()

newCsv = []
output = 'amazon_utf_problems_ftfy.csv'
newFile = open(output, 'w') #wb for windows, else you'll see newlines added to csv

# open the file from console arguments
with open(filename, 'r', encoding='utf8') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		newCsv.append(row)
writer = csv.writer(newFile)

header_row1 = ('original', 'fixed')
writer.writerow(header_row1)

count = 0
errors = 0
for item in newCsv:

	text1 = item['title']
	fixed = fix_encoding(text1)

	write_tuple = (text1, fixed)
	writer.writerow(write_tuple)

	#text2 = item['product_description']

	#fixed = fix_encoding(text2)
	#fixed = fix_text(fixed)
	#write_tuple = (text2, fixed)
	#writer.writerow(write_tuple)

	#print(ftfy.fix_file('Highsmith_Errors_only2.csv'))
	#print(text2)
	#print(fix_encoding(text2))
	#print(text2.decode('latin1'))
	#print(item['item_name'].decode('utf8').encode('latin1').decode('utf8'))
	#print(fix_text(['item_name'].decode('utf8').encode('latin1').decode('utf8')))
	#print(fix_encoding(item['item_name'].decode('utf8').encode('latin1').decode('utf8')))