INPUT_PDF = 'Full.pdf'
STARTING_PAGE = 3

# contents
PARTS = [( 3, 8, 'Lab01 - Python basics'),
         (11, 5, 'Lab02 - Python files and OS'),
         (16, 9, 'Lab03 - Python OOP and GUI'),
         (25, 6, 'Lab04 - Python libraries'),
         (31, 3, 'Back')]


from PyPDF2 import PdfFileWriter, PdfFileReader


pdf = PdfFileReader(open(INPUT_PDF, 'rb'))

for part in PARTS:
    writer = PdfFileWriter()
    # add all pages to the current part of pdf file
    starting_page = part[0] - STARTING_PAGE
    for page in range(part[1]):
        writer.addPage(pdf.getPage(starting_page + page))
    # write pdf fragment to another pdf
    with open(part[2] + '.pdf', 'wb') as pdf_stream:
        writer.write(pdf_stream)
