#!/usr/bin/python3

import re

#have user input the accession number
accession = input('Enter Accession Number inside single quotes: ')

#open and read file
with open("/home/kprecht2/unit03/e_coli_k12_dh10b.faa") as file:
	my_file_contents = file.read()
	#split the contents by the > symbol. This will be used for the regex later
	genes = my_file_contents.split('>')

#create a look to search through genes and find the accession number
for gene in genes:
	if re.findall(accession, gene):
		#if the results are found, print the FASTA entry
		print '>' + gene



