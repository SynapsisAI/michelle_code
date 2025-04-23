_Source_
- https://www.youtube.com/watch?v=QVTZ8f9l1Ko: How I Parse 99% of PDFs into Structured Data
+ Use LLamaIndex to do Lllama parsing
+ Use Structured Output from OpenAI
+ supbase: open source Firebase aleternative
+ automate the whole proc3ss: n8n connecting supabase databse, OpenAI API and LlamaIndex
=> Build an entire Extraction Pipeline

* Note that we can have an ordinary RAG model combined with LLM to do data retrieval tasks 
based on unstructured question. This system is good at finding relevant parts to answer a 
question. But when we use this to parse complex documents, it starts to fall apart.

RAG + LlamaParse: Advanced PDF Parsing for Retrieval:
* "LlamaParse is a generative AI enabled document parsing technology designed for complex documents that contain embedded objects like tables and figures. Ingest Complex Documents with LlamaParse."

# What is parsing
* parsing is the process of analysing unstructured and structure it to structured format that LLMs can understand
* Example: pdf: dissect pdf to extract specific fields, like name, date, transaction => Understand the structure and data to extract with precision
* automate the parsing objects, make it accurate and reliable
* structured documents: invoices, legal documents,... => easier to extract
* more unstructured documents: financial document, pdf with listing property => the model has not seen the format before, and thus woul fail.
* Use **LlamaParse** from LlamaIndex: open-sourced, specially designed for LLM application. We can convert the text, and can even convert a graph into a table.  https://www.llamaindex.ai/llamaparse

# When using the LlamaParse model, there are different parameters, and we have to choose the set of parameters that best fits our context.
* Go to https://cloud.llamaindex.ai/project/482b8bfe-889b-4ef2-b985-3689168a075b/parse
* Play around which set of parameters is the best first
* Besides Parsing, there's also (1) Extraction and (2) Indexing functions.

# Flow
File -> Llama Parse -> make API request to check if the job on Llama Parse is complete or not -> grab content in md/json format  -> parse it to OpenAI Structured Output -> Insert to Supabase
Define the JSON Schema to extract data from the md output for the OpenAI Structured Output
Make sure the schema matches the Supabase table