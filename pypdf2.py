import PyPDF2
pdfFileObj = open("1.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
mytext = ""
for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    mytext += pageObj.extractText()
print(mytext)
with open('1.txt', 'w') as f:
    f.write(mytext)
pdfFileObj.close()