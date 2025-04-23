# If cannot push to Github repository due to conflicts in SSH Keys, do:
`ssh -T git@github-michelle`
`git remote -v`
# Important links to understand why it's so hard to find the structure in PDF
- https://stackoverflow.com/questions/937808/how-to-extract-data-from-a-pdf-file-while-keeping-track-of-its-structure
- https://stackoverflow.com/questions/22675690/if-identifying-text-structure-in-pdf-documents-is-so-difficult-how-do-pdf-reade/
- Some suggested that we should convert PDF to markdown and work from there.
- https://nanonets.com/blog/document-parsing/
- Best PDF Parser for Academic Papers: https://www.reddit.com/r/Rag/comments/1ilxf1i/best_pdf_parser_for_academic_papers/


# Approaches
1. Use LLamaParse, we have quite a decent Markdown version of pdf. Need to figure out a way to remoe all the unnecessary # headings in between the section text.
- Can try to put the Markdown output as input of ChatGPT and ask chatgpt to produce output, but so far the output is bad, and using double LLM just increases work load.

2. Use RAG approach by Thu Vu, but this approach is to break the pdf down into smaller chunks, and return only the relevant parts to answer a specific question. Why do we need to break down to chunks? If this approach does not work, do we cancel out all the RAG methods? In the Youtube video parsing 99% content of PDF he said RAG ony finds relevant information to answer an unstructured question, and will fall apart at parsing complex documents.
    - If it's for a RAG, you don't need to parse them, you can just compute the embedding of the pages with Colpali https://huggingface.co/blog/manu/colpali (and like the other said Gemini does the job for text extraction)

3. We can also explore the variety of options out there, from Reddit, Quora and Stack Overflow:
- LLamaParse
- science-parse: https://github.com/allenai/science-parse
- Docling: https://github.com/docling-project/docling
    + OCR support is also present.
    + Integrates easily with LLM app / RAG frameworks.
    + Inbuilt Hierarchical Chunking is also supported.    
    + I tried this but it’s bad at parsing inline equations
- GROBID: https://github.com/kermitt2/grobid -> Specialised for scientific research papers
- science-parse: https://github.com/allenai/science-parse
- Unstructured.io: can be run locally
- TIKA Parser, It can run locally using a server link. Some say it's better than Unstructuredx
- Nougat (hasn’t been updated in a while)
- 
---
**Other less popular options**

- PyMuPDF4llm: https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/
    + internal order and table markdown could be not as perfect in comparison to Docling. It has different heading levels
- PDF files can be parsed with tabula-py, or tabula-java: https://aegis4048.github.io/parse-pdf-files-while-retaining-structure-with-tabula-py
- PDFBox https://pdfbox.apache.org/ is a PDF parsing tool that you can use for extracting text and images on top of which you can define your custom rules for parsing.
- Texify/marker:
    + tries to convert pdfs into markdown and they convert math equations into latex in that markdown
    + But the latex sometimes can be inaccurate. For that part, you can try different latex ocrs by passing the specific page with incorrect latex again to other tools.(This will depend on your usecase and how you create your pipeline.) 
- poppler and surya ocr for parsing pdfs.
- layoutlmv3
- blip
- Qwen 2.5 VL Instruct?
    + converting each page to pngs
    + then use Qwn
    + I used Qwen 2 VL Instruct to parse financial academic papers using this method and the results were good enough to work with; I needed to implement another section in the pipeline to clean up the math equations into LaTeX
- https://itextpdf.com/

4. Use other LLM: Gemini flash 2.0. llama 3.3; but need to have the correct approach
* think about what domain something is in. This will help the model understand the nuances that docling is struggling with.
think about what it needs to get absolutely right (e.g inline equations, tables, etc).
* Then, process 5 random documents to check painfully if the job is alright. If not, tune prompts, go again.
* I'd generally do it at either a page level or if the doc is small enough, just at the doc level.
* Quite similar to this, conceptually: https://generative-ai-newsroom.com/structured-outputs-making-llms-reliable-for-document-processing-c3b6b2baed36 Give it a read, and use the concepts around document processing here. I suspect you won't need it to the degree of the OCR stuff etc., but still good to know.
* Try to iterate and get it right on a few documents before you turn it full throttle for your entire dataset!

---
***

# Direction to go:
1. Extract structured data from PDF: text, image, sections and title section. Need recognition from AI. Mutimodal RAG.
2. Do a summary script.
2. Extract text from image: to generate a description for image => Image+Video Selection Model.
3. AI voiceover
4. Combine into a video

# Resources below:
# 1-From PDF to Text, image and other structured data
- https://www.youtube.com/watch?v=EFUE4DHiAPM: Extracting Structured Data From PDFs | Full Python AI project for beginners (ft Docker) (use LLM: Structured Output from OpenAI)
- https://www.youtube.com/watch?v=G0PApj7YPBo: Extract text, links, images, tables from Pdf with Python | PyMuPDF, PyPdf, PdfPlumber tutorial
- https://www.youtube.com/watch?v=Ymq8o7FSoVc: Unstract: AI Document Parser: Extract Data from Complex PDFs at Scale! (Open Source) #use UNSTRACT (PAID)
- https://www.youtube.com/watch?v=lkdYxiGUFUA: Extract Data from PDFs Easily & Quickly (table form/image/text/pages) #Use PDFELEMENT (PAID)
- https://www.youtube.com/watch?v=J3d6bx3i4l0: Microsoft AI Builder Tutorial - Extract Data from PDF (Use Microsoft AI Builder - paid)
- https://www.youtube.com/watch?v=QVTZ8f9l1Ko: How I Parse 99% of PDFs into Structured Data
+ Use LLamaIndex
+ Use Structured Output from OpenAI
+ supbase: open source Firebase aleternative
+ automate the whole proc3ss: n8n connecting supabase databse, OpenAI API and LlamaIndex
=> Build an entire Extraction Pipeline
# 2 - RAG Model
- https://www.youtube.com/watch?v=uLrReyH5cu0: Multimodal RAG: Chat with PDFs (Images & Tables) [2025]
- https://www.youtube.com/watch?v=2TJxpyO3ei4: Python RAG Tutorial (with Local LLMs): AI For Your PDFs
- https://www.youtube.com/watch?v=ABK00e2XdPo: Realtime Multimodal RAG Usecase Part 1 | Extract Image,Table,Text from Documents #rag #multimodal

# 3-Convert pdf to TEXT only
- https://medium.com/@harikrishnank497/how-to-convert-a-pdf-file-to-a-txt-file-locally-using-python-bc82c1403749
- https://stackoverflow.com/questions/76093737/convert-edited-pdf-into-txtm
- https://community.openai.com/t/whats-the-appropriate-way-to-convert-pdfs-to-text-files/123764
- https://www.reddit.com/r/LangChain/comments/1e7cntq/whats_the_best_python_library_for_extracting_text/
- https://discuss.python.org/t/convert-pdf-into-txt/25717
- https://ploomber.io/blog/pdf-ocr/
- https://docs.aspose.com/pdf/python-cpp/convert-pdf-to-other-files/
- https://medium.com/@alexaae9/5-ways-to-convert-pdf-to-word-in-python-a-comparison-guide-1771cfd109e7
- https://www.youtube.com/watch?v=RULkvM7AdzY: Extract Text from any PDF File in Python 3.10 
- https://www.youtube.com/watch?v=BFl6V4sIcWQ: Convert PDF to Text: Python PDFminer example using Python
- https://www.youtube.com/watch?v=0B5N6Xt5K8Q: Extract Text from PDF with Python
- https://www.youtube.com/watch?v=k2O-r9K1-gA: How to Convert PDF to Text in Python
- https://www.youtube.com/watch?v=w2r2Bg42UPY: Extract PDF Content with Python
- https://www.youtube.com/watch?v=j5kaCiWOyww: Extract Text From PDF File In 90 Seconds Using Python

# 4- Summarise information from PDF
- https://www.youtube.com/watch?v=CgHy3uq7x6A&list=PLcP8bHQl_w-F9RZeczGmJc16XoRHSiGQz: Extract Key Information From Documents Using DocQuery | Extract Text | LayoutLM
- https://www.youtube.com/watch?v=xZzvwR9jdPA: Use LLMs To Extract Data From Text (Expert Mode)
- https://www.youtube.com/watch?v=5Ghv-F1wF_0: Learn How To Query Pdf using Langchain Open AI in 5 min

# 5- How to get Data Ready for AI Agents
- https://www.youtube.com/watch?v=9lBTS5dM27c&t=13s: How to Get Your Data Ready for AI Agents (Docs, PDFs, Websites)

# 6- Extract text from image
- https://www.youtube.com/watch?v=00zR9rJnecA: https://www.youtube.com/watch?v=00zR9rJnecA: Best OCR Models to Extract Text from Images (EasyOCR, PyTesseract, Idefics2, Claude, GPT-4, Gemini)
- https://www.youtube.com/watch?v=nnZRBAzW3CA: Extract Text from PDFs & Images for LLMs Using Python


