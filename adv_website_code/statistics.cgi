#!/usr/local/bin/python3

import jinja2
import cgi
import mysql.connector
from decimal import Decimal

def main():
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates")

    env = jinja2.Environment(loader=templateLoader)
    template = env.get_template("statistics_final.html")	

    #connect to a database
    conn = mysql.connector.connect( user='kprecht2', password='Ma$on2017',
                                        host='localhost', database='kprecht2')
    cursor = conn.cursor()

    qry = """ SELECT count(distinct(allele_id)) as num_genes
	, count(*) as total_num_snps 
	FROM snp_location l 
	WHERE chrom = %s
	"""

    cursor.execute(qry, (6, ))
    results6 = cursor.fetchall()

    cursor.execute(qry, (7, ))
    results7 = cursor.fetchall()

    cursor.execute(qry, (16, ))
    results16 = cursor.fetchall()

    cursor.execute(qry, (17, ))
    results17 = cursor.fetchall()

    qry_size = """ SELECT (sum(size)) FROM (
	SELECT (bp_end - bp_start) as size
	FROM chromosome
	WHERE chromosme = %s) ps
	 """
    
    cursor.execute(qry_size, (6, ))
    size6  = cursor.fetchone()
    #get rid of decimal number
    chrom6 = str(size6)
    chrom6_size =  (chrom6[10:19])

    cursor.execute(qry_size, (7, ))
    size7 = cursor.fetchone()
    #get rid of decimal numbers
    chrom7 = str(size7)
    chrom7_size = (chrom7[10:19])

    cursor.execute(qry_size, (17, ))
    size17 = cursor.fetchone()
    #get rid of decimal number
    chrom17 = str(size17)
    chrom17_size = (chrom17[10:18])

    cursor.execute(qry_size, (16, ))
    size16 = cursor.fetchone()
    chrom16 = str(size16)
    chrom16_size = (chrom16[10:19])

    conn.commit()		
    cursor.close()

    print("Content-Type: text/html\n\n")
    print(template.render(results6=results6, results7=results7, results16=results16,  results17=results17,  chrom16_size=chrom16_size, chrom6_size=chrom6_size, chrom7_size=chrom7_size, chrom17_size=chrom17_size))


if __name__ == '__main__':
    main()
