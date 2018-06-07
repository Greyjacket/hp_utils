import csv, sys, math, operator, re, os
from ftfy import fix_encoding, fix_text

try:
	filename = sys.argv[1]
except:
	print ("\nPlease input a valid CSV filename.\n")
	print ("Format: python scriptname filename.\n")
	exit()

newCsv = []
output = 'amazon_utf_problems.csv'
newFile = open(output, 'w', newline='') 

# open the file from console arguments
with open(filename, 'r', encoding='utf8') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		newCsv.append(row)
writer = csv.writer(newFile)

header_row1 = ('item_sku', 'title', 'description', 'bullet5', 'keywords')
writer.writerow(header_row1)

decoding = 'ascii' #ascii, latin1, utf8
encoding = 'latin1'
for item in newCsv:

	dirty = False;

	try:
		item_name = item['item_name'].encode(encoding).decode(decoding)
		item_name = ""
	except:
		dirty = True
		item_name = (item['item_name'])
	try:		
		product_description = item['product_description'].encode(encoding).decode(decoding)
		product_description = ""
	except Exception as e:
		dirty = True
		product_description = (item['product_description'])

	try:	
		bullet5 = item['bullet5'].encode(encoding).decode(decoding)
		bullet5 = ""
	except:
		dirty = True
		bullet5 = (item['bullet5'])

	try:
		keywords = item['keywords'].encode(encoding).decode(decoding)	
		keywords = ""
	except:
		dirty = True
		keywords = (item['keywords'])

	if dirty:
		write_tuple = (item['item_sku'], item_name, product_description, bullet5, keywords)
		writer.writerow(write_tuple)

newFile.close()