#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

def main():

    print("Content-Type: application/json\n\n")

    form = cgi.FieldStorage()
    term = form.getvalue('search_term')

    conn = mysql.connector.connect( user='kprecht2', password='Ma$on2017',
                                        host='localhost', database='kprecht2')
    cursor = conn.cursor()

    qry = """
          SELECT vr.variation_name
        , vr.variant_type
        , vr.phenotype
        , vr.significance
        , g.gene_symbol
        , vr.omim_id                                         
        FROM snp_variation_results vr
        LEFT JOIN snp_genes g on g.gene_id = vr.gene_id
        WHERE vr.phenotype like %s

    """
    cursor.execute(qry, ('%' + term + '%', ))

    results = { 'match_count': 0, 'matches': list() }
    for (variation_name, variant_type, phenotype, significance, gene_symbol, omim_id) in cursor:
        results['matches'].append({'variation_name': variation_name, 'variant_type': variant_type, 'phenotype': phenotype, 'significance': significance, 'gene_symbol': gene_symbol, 'omim_id': omim_id})
        results['match_count'] += 1

    conn.close()

    print(json.dumps(results))

if __name__ == '__main__':
    main()
