import csv
import pdfplumber
pdf_fname = '2.pdf'

outfile = open('2.csv', 'w')
outcsv = csv.writer(outfile)

pdf = pdfplumber.open(pdf_fname)
for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  # note how I'm still skipping the header
        outcsv.writerow(row)
outfile.close