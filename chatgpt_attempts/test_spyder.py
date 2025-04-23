import os
os.chdir("/Users/michellenguyen/Documents/ECHALLENGE_SYNAPSIS/")
file_path="NIPS-2017-attention-is-all-you-need-Paper.pdf"

from pypdf import PdfReader
reader= PdfReader(file_path)
page = reader.pages[5]
for i in page.images: #page
    #open a file named string i.name, write binary
    with open(i.name, 'wb') as f:
        f.write(i.data)

import pdfplumber
with pdfplumber.open(file_path) as f:
    for i in f.pages:
        print(i.extract_tables())