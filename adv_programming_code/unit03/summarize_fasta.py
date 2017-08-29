#!/usr/bin/python3

import re

#open and read file
with open("/home/kprecht2/unit03/e_coli_k12_dh10b.faa") as file:
	my_file_contents = file.read()
	#split the contents by the > symbol. This will be used for the regex later
	genes = my_file_contents.split('>')
	#split the contents and remove the first line. This will be used for the calculations
	sequences = re.split(r'>.+?\n', my_file_contents)

#count the number of gene enteries in file
gene_count = len(sequences)
print "My gene count is " + str(gene_count)

#create a loop to look at the length of each sequence in the file
list_protein_lengths = []
for seq in sequences:
	protein_length = len(seq)
	list_protein_lengths.append(protein_length)

#calculate the max and min protein length and print it to screen
print "The min protein length is " + str(min(list_protein_lengths))
print "The max protein length is " + str(max(list_protein_lengths))

#create a loop to look at the file split early by the > symbol. 
list_of_matches = []
for gene in genes:
	#use regex to find all genes with hypothetical in the title
	matches = re.findall(r'hypothetical', gene)
	match_count = len(matches)
	list_of_matches.append(match_count)

#print the number of matches
print "There are " + str(sum(list_of_matches)) + " genes with " + \
	  "hypthotetical in the description"
