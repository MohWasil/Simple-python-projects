import PyPDF2 as pdf
pdf_opener = pdf.PdfReader(open('./combined.pdf', 'rb'))
watermark = pdf.PdfReader(open('./wtr.pdf', 'rb'))
output = pdf.PdfWriter()
for x in range(len(pdf_opener.pages)):
    page = pdf_opener.pages[x]
    page.merge_page(watermark.pages[0])
    output.add_page(page)
with open('watermarked.pdf', 'wb') as file:
    output.write(file)

