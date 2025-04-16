"""
use langchain summarization chain
"""
#Install openai, langchain, tiktoken libraries using pip.
#`!pip3 install -q gradio openai pypdf langchain`


#Creating OpenAI key
from openai import OpenAI
from dotenv import load_dotenv #pip install python-dotenv
import os

# Load environment variables from .env file
load_dotenv()

#****Basic Example
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


#import libraries
import gradio as gr
from langchain import OpenAI, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader
llm = OpenAI(api_key=os.environ.get("my_test_key"),temperature=0) #use the default model of langchain: test-darwin something
#llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106",api_key=os.environ.get("my_test_key"))
#llm = ChatOpenAI(temperature=0, model_name="gpt-4o",api_key=os.environ.get("my_test_key"))

#Defining the summarization function
def summarize_pdf(pdf_file_path):
    loader = PyPDFLoader(pdf_file_path)
    docs = loader.load_and_split()
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(docs)   
    return summary
#summary_new = summarize_pdf("/Users/michellenguyen/Documents/ECHALLENGE_SYNAPSIS/tech-echallenge-git-organisation/week1_michelle_test_summary/NIPS-2017-attention-is-all-you-need-Paper.pdf")

#Use GRADIO
#Gradio is an open-source Python package that allows you to quickly create and share interactive web applications for machine learning models, APIs, or any Python function, with a focus on ease of use and rapid developmen
#Setting up the user Interface using Gradio: Gradio provides UI where you can upload pdf path and summary will be displayed
input_pdf_path = gr.components.Textbox(label="Provide the PDF file path")
output_summary = gr.components.Textbox(label="Summary")

interface = gr.Interface(
    fn=summarize_pdf,
    inputs=input_pdf_path,
    outputs=output_summary,
    title="PDF Summarizer",
    description="Provide PDF file path to get the summary.",
).launch(share=True)

#gr.close_all() #close all gradio ports