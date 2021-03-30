import PyPDF2
def encrypt_pdf(file,password):
    pdfFile = open(file, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfWriter.encrypt(password)
    
    en_file = 'encrypted_' + file
    resultPdf = open(en_file, 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()