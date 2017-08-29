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

    qry = """ SELECT allele_id, phenotype
        FROM snp_variation_results
        WHERE phenotype like %s
        LIMIT 5 """

    cursor.execute(qry, ('%' + term + '%', ))

    results = list()

    for (allele_id, phenotype) in cursor:
        results_dictionary = dict({'value': allele_id, 'label': phenotype})
        results.append(results_dictionary)

    conn.close()

    print(json.dumps(results))


if __name__ == '__main__':
    main()
