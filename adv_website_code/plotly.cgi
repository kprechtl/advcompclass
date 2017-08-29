#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

def main():

    print("Content-Type: application/json\n\n")

    form = cgi.FieldStorage()
    term = form.getvalue('term')

    conn = mysql.connector.connect( user='kprecht2', password='Ma$on2017',
                                        host='localhost', database='kprecht2')
    cursor = conn.cursor()

    #run a query to find the chromosome that the search term is on
    qry1 = """
	SELECT distinct(l.chrom), concat(cytogenic, '%')
 	 FROM snp_variation_results vr
  	 JOIN snp_location l on vr.allele_id = l.allele_id
 	 WHERE vr.variation_name LIKE %s
	"""

    cursor.execute(qry1, (term, ))
    chrom_name_list = cursor.fetchone() 
    chrom_name = chrom_name_list[::-1]

    #run another query that uses the chromosome name found in the first query to obtain the chrom information
    qry = """
	SELECT chromosme
	  , name
	  , size
	  , case when uniq_color like %s then 'mediumspringgreen' 
	  when uniq_color like '%gpos' then 'black'
	  when uniq_color like '%gneg' then 'lightgray'
	  when uniq_color like '%cen' then 'lightgray'
	  else uniq_color end as color
	FROM (
	  SELECT chromosme
  	  , CONCAT(band, arm) as name
  	  , (bp_end - bp_start) as size
   	  , CONCAT(chromosme, arm, band, stain) as uniq_color
  	  , CASE WHEN stain LIKE 'gpos' THEN 'black' ELSE 'lightgray' END as color
	FROM chromosome
  	WHERE chromosme = %s ) ps 
	"""
    cursor.execute(qry, chrom_name)

    #put the results in a plotly JSON format so that I can grath this information
    results = {'matches': list() }
    for (chromosome, name, size, color) in cursor:
        decoded_color = color.decode("utf-8")
        results['matches'].append({'name': chromosome, 'text': name, 'x': [size], 'marker' : {'color': decoded_color}, 'type': 'bar'})

    conn.close()

    print(json.dumps(results))

if __name__ == '__main__':
    main()
