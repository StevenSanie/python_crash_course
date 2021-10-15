from PyPDF2 import PdfFileReader as pdfReader
def grab(filename):
	with open(filename, 'rb') as f:
		pdf = pdfReader(f)
		data = pdf.getDocumentInfo()
		number_of_pages = pdf.getNumPages()
		print(f"""
		Author: {data.author}
		Creator: {data.creator}
		Producer: {data.producer}
		Subject: {data.subject}
		Title: {data.title}
		Number Of Pages: {number_of_pages}
		
		""")

grab('Books/Steve Jobs.pdf')