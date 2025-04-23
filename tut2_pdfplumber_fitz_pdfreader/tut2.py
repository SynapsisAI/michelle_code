"""_Source_

https://www.youtube.com/watch?v=G0PApj7YPBo
Extract text, links, images, tables from Pdf with Python | 
PyMuPDF, PyPdf, PdfPlumber tutorial
"""

#pip install pypdf
from pypdf import PdfReader
file_path="/Users/michellenguyen/Documents/ECHALLENGE_SYNAPSIS/NIPS-2017-attention-is-all-you-need-Paper.pdf"
reader= PdfReader(file_path)
#see the length of pages of pdf
print(len(reader.pages))
#grab the first page text content
page = reader.pages[0]
print(page.extract_text()) #extract_text() method #note that all tables and non-paragraph data is also pasted as text
#print text of every page
#for i in range(len(reader.pages)):
    #page = reader.pages[i]
    #print(page.extract_text())
#grab images
for i in page.images: #page
    #open a file named string i.name, write binary
    with open(i.name, 'wb') as f:
        f.write(i.data)

#pip install pdfplumber #to use to extract table
import pdfplumber
with pdfplumber.open(file_path) as f:
    for i in f.pages:
        print(i.extract_tables())

#pip install pymupdf
import fitz
doc = fitz.open(file_path)
print(doc.page_count)
print(doc.metadata) #format, title, author, subject, creator, producer, encryption
page = doc.load_page(0)
print(page.get_text())
#save the first page as image
pix = page.get_pixmap()
pix.save(f"page_{page.number}.png")
#get the links from pdf
links = page.get_links()
print(links) #can represent this as a dataframe to see all different links