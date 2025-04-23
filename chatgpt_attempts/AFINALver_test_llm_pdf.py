import fitz  # PyMuPDF
import camelot  # Camelot for tables
import re
import base64
import json
#import os
#os.chdir(path)

# ─── Utility Functions ─────────────────────────────────────────────────────────

def extract_pages(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for page in doc:
        text = page.get_text("text")
        blocks = page.get_text("dict")
        images = []
        for img in page.get_images(full=True):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            img_data = pix.tobytes("png")
            images.append({"xref": xref, "data": img_data})
        pages.append({"text": text, "blocks": blocks, "images": images})
    return pages

def extract_tables(pdf_path):
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='lattice')
    result = [t.df.to_dict(orient="split") for t in tables]
    return result

SECTION_HEADERS = [
    r"^(?:Abstract)$",
    r"^(?:\d+\s+Introduction)$",
    r"^(?:\d+\s+.+)$",  # covers "2 Background", "3 Model Architecture", etc.
    r"^(?:Results)$",
    r"^(?:Conclusion)$",
    r"^(?:References)$"
]
HEADER_RE = re.compile("|".join(SECTION_HEADERS), re.IGNORECASE)

def split_sections(full_text):
    lines = full_text.splitlines()
    sections = {}
    current = None
    for line in lines:
        if HEADER_RE.match(line.strip()):
            current = line.strip()
            sections[current] = []
        elif current:
            sections[current].append(line)
    return {sec: "\n".join(text).strip() for sec, text in sections.items()}

def extract_authors(pdf_path):
    doc = fitz.open(pdf_path)
    page0 = doc[0]
    full_text = page0.get_text("text")
    header, _ = full_text.split("Abstract", 1)
    lines = [l.strip() for l in header.splitlines() if l.strip()]
    title = lines[0]
    author_lines = lines[1:]
    authors = []
    email_regex = re.compile(r"\S+@\S+")
    for idx, line in enumerate(author_lines):
        if email_regex.search(line):
            email = line
            affiliation = author_lines[idx - 1] if idx >= 1 else ""
            name = author_lines[idx - 2] if idx >= 2 else ""
            authors.append({
                "name": name,
                "affiliation": affiliation,
                "email": email
            })
    return title, authors

# ─── Main Pipeline ────────────────────────────────────────────────────────────
pdf_path="/Users/michellenguyen/Documents/ECHALLENGE_SYNAPSIS/NIPS-2017-attention-is-all-you-need-Paper.pdf"
pages = extract_pages(pdf_path)
tables = extract_tables(pdf_path)
full_text = "\n".join(p["text"] for p in pages)
sections = split_sections(full_text)
title, authors = extract_authors(pdf_path)


#-----------------
def build_json_from_pdf(pdf_path, output_json):
    # Extract raw content
    pages = extract_pages(pdf_path)
    tables = extract_tables(pdf_path)
    full_text = "\n".join(p["text"] for p in pages)
    sections = split_sections(full_text)
    title, authors = extract_authors(pdf_path)

    # Build base structure
    doc_json = {
        "Title": title,
        "Authors": authors,
        "Abstract": sections.get("Abstract", ""),
        "Introduction": {
            "Text": sections.get("1 Introduction", ""),
            "Images": [],
            "Tables": []
        },
        "Methods": {
            "Text": sections.get("2 Background", ""),
            "Images": [],
            "Tables": []
        },
        "Results": {
            "Text": sections.get("Results", ""),
            "Images": [],
            "Tables": []
        },
        "Conclusion": {
            "Text": sections.get("Conclusion", ""),
        },
        "References": sections.get("References", "").splitlines()
    }

    # Encode images to base64 and attach (simple example: all images in doc)
    for sec_key in ["Introduction", "Methods", "Results"]:
        for img in pages[0]["images"]:  # for demo, attach first-page images to intro
            b64 = base64.b64encode(img["data"]).decode()
            doc_json[sec_key]["Images"].append({"xref": img["xref"], "base64": b64})

    # Attach all tables to Results (demo)
    doc_json["Results"]["Tables"] = tables

    # Write JSON out
    with open(output_json, "w") as f:
        json.dump(doc_json, f, indent=2)

    print(f"JSON saved to {output_json}")

# ─── Execute ─────────────────────────────────────────────────────────────────
file_path="/Users/michellenguyen/Documents/ECHALLENGE_SYNAPSIS/tech-echallenge-git-organisation/michelle_code/tut3_llma_parse_rachid/data/han_qsar.pdf"
if __name__ == "__main__":
    build_json_from_pdf(file_path,"paper_structured.json")

