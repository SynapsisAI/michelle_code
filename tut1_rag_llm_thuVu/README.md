_Tutorial link_
https://www.youtube.com/watch?v=EFUE4DHiAPM: Extracting Structured Data From PDFs | Full Python AI project for beginners (ft Docker)

Title: Extracting Structured Data From PDFs | Full Python AI project for beginners (ft Docker)

* Have a system that automatically extracts necesary information from unstructured data: PDFs books, business invoices, customer queries emails, images, and condense information into a table we define
* One of the best thing of AI: Information retrieval from a knowledge base/ sifting through heaps of report and organising them to structured format like excel
1. LLM model chatgpt 4.0
2. Build a document retrieval system
3. Get answers in a structured format (made possible due to STRUCTURED OUTPUT from OPEN AI)
4. Cite the exact text sources (should point to the exact point of the document from the summaryed text portion)
5. Build the Streamlit app for user interface
6. Build the app with Docker.

This kind of system to retrieve information: "Retrieval Augmented Generation (RAG)"
RAG: What is Bill Gates' salary according to documents?
Normal question: What is Bill Gates' salary?

* great when knowledge base contains proprietary
* LLMs hallucinate
* RAG: avoid
* avoid hallucination
* system refuses to answer if lacking context
* cite data sources where answer is based
RAG > Fine-Tuning a LLM using a custom language base 

A RAG
1. Retrieval: process documents
2. Retrieval: query for relevant parts of the document that may contain the response based on the user's question
3. Augmented Generation: 
- craft the response based on LLM of choice (Augmented Generation) like ChatGPT, or ClaudeAI
- utilise the reasoning capability of LLM to generate highly accurate and relevant responses based on the retrieved information

Create a new python environment in a sub directory in the folder:
`python3 -m venv myenv`
After that activate using:
`source myenv/bin/activate`

Other LLM models besides ChatGPT
- openAI chatGPT
- Ahthropic: Claude LLM
- Mistral AI
- open-sourced local LLM like Llama 3

**Watched until 26:08 / 36:23** of the video.