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
	select case when significance like '%benign%' then 10 
	when significance like '%uncertain%' then 65
	when significance like '-' then 65
	when significance like '%risk factor%' then 99
	when significance like '%drug response%' then 154
	when significance like '%conflicting%' then 65
	when significance like '%pathogenic%' then 180
	when significance like '%association%' then 135
	when significance like '%affects%' then 115
	when significance like '%not provided%' then 48
	when significance like '%other%' then 25 
	else significance end as significance
	from snp_variation_results
	where variation_name like %s
	"""

    cursor.execute(qry1, (term, ))
    cursor = cursor.fetchone()

    #put the results in a plotly JSON format so that I can grath this information
    results = {}
    for significance in cursor:
        results["matches"] = significance

    conn.close()

    print(json.dumps(results))

if __name__ == '__main__':
    main()
