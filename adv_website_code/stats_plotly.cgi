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
	SELECT count(allele_id), concat('chrom', chrom) as chrom
 	 FROM snp_location l
 	 GROUP BY chrom
	"""

    cursor.execute(qry1)
    my_results = cursor.fetchall()

    x = []
    y = []
    for result in my_results:
        y.append(result[0])
        decoded_name = (result[1]).decode("utf-8")
        x.append(decoded_name) 

    #put the results in a plotly JSON format so that I can grath this information
    results = {'matches': list() }
    results['matches'].append({'name': x,  'x': x, 'y': y, 'marker' : {'color': 'mediumspringgreen'}, 'type': 'bar'})

    conn.close()

    print(json.dumps(results))

if __name__ == '__main__':
    main()
