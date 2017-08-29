#!/usr/local/bin/python3

import jinja2
import cgi
import mysql.connector

def main():
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates")

    env = jinja2.Environment(loader=templateLoader)
    template = env.get_template("snp_info.html")	

    form = cgi.FieldStorage()
    term = form.getvalue('term')

    #connect to a database
    conn = mysql.connector.connect( user='kprecht2', password='Ma$on2017',
                                        host='localhost', database='kprecht2')
    cursor = conn.cursor()

    qry_info = """
	SELECT vr.variation_name, vr.allele_id
	, vr.gene_id, g.gene_symbol, g.hgnc_id
	, vr.variant_type, vr.phenotype
	, significance
	FROM snp_variation_results vr
	JOIN snp_genes g on g.gene_id = vr.gene_id
	WHERE variation_name like %s
	 """
    
    cursor.execute(qry_info, (term, ))
    results8  = cursor.fetchall()

    loc_qry = """
	SELECT chrom, chrom_start, chrom_end, ref_allele, alt_allele, cytogenic
	FROM snp_variation_results vr
	JOIN snp_location l on l.allele_id = vr.allele_id
	WHERE variation_name like %s
        LIMIT 1
	"""

    cursor.execute(loc_qry, (term, ))
    loc_results = cursor.fetchall()
    conn.commit()		
    cursor.close()

    print("Content-Type: text/html\n\n")
    print(template.render(results8 = results8, term=term, loc_results = loc_results))


if __name__ == '__main__':
    main()
