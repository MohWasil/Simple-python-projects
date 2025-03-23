import PyPDF2 as pdf
import sys

inputs = sys.argv[1:]

def Pdf_combiner(pdf_list):
    combine = pdf.PdfMerger()
    for pdfs in pdf_list:
        combine.append(pdfs)
        print('Done!')
    combine.write('combined.pdf')
Pdf_combiner(inputs)
