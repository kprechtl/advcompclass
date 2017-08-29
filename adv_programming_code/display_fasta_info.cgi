#!/usr/local/bin/python3

import jinja2
import re

# This line tells the template loader where to search for template files
templateLoader = jinja2.FileSystemLoader( searchpath="./templates" )

# This creates your environment and loads a specific template
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('unit04.html')

# PARSE the fasta file 

with open("/Users/kimprechtl/Desktop/test.faa") as file:
	my_file_contents = file.read()
	#split the contents by the > symbol. This will be used for the regex later
	genes = my_file_contents.split('>')

id_match_list = []
header_match_list = []
seq_length_list = []

#create a look to search through genes and find the accession number
for gene in genes:

	#find all id's in each fasta file
	id_match = re.findall(r'gi.+?(?=\[)', gene)
	id_match_list.append(id_match)

	#find all headers in fasta file
	#the regex looks behind and in front for a bracket (?<= and ?=)
	header_match = re.findall(r'(?<=\[).+?(?=\])', gene)
	header_match_list.append(header_match)

	#find all sequences in fastafile
	sequence_match = re.split(r'gi.+?\n', gene)
	#join sequences together
	seq = ''.join(sequence_match)
	#find sequence length
	seq_length = len(seq)
	seq_length_list.append(seq_length)

#join the 3 lists together 
new_list =[]
new_list = zip(id_match_list, header_match_list, seq_length_list)
final_list = new_list[1:]


print("Content-Type: text/html\n\n")
print(template.render(final_list=final_list))


