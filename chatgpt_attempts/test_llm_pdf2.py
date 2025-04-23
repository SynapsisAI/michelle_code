import fitz
"""
This works:
    Use this:

    pip install --upgrade pymupdf
    This will install from a Python wheel if one is available for your platform
    
    https://pymupdf.readthedocs.io/en/latest/installation.html#option-2-install-from-binaries
"""
import camelot
import re
import json
import os
import matplotlib.pyplot as plt

def extract_pages(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text("text")
        images = []
        for img in page.get_images(full=True):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            img_path = f"images/page{i+1}_img{xref}.png"
            os.makedirs(os.path.dirname(img_path), exist_ok=True)
            pix.save(img_path)
            images.append(img_path)
        pages.append({"text": text, "images": images})
    return pages

def extract_tables_and_save(pdf_path):
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='lattice')
    table_paths = []
    for idx, t in enumerate(tables):
        df = t.df
        fig, ax = plt.subplots(figsize=(8, df.shape[0] * 0.5))
        ax.axis('off')
        tbl = ax.table(cellText=df.values, colLabels=df.columns, loc='center')
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(10)
        table_path = f"images/table_{idx}.png"
        os.makedirs(os.path.dirname(table_path), exist_ok=True)
        fig.savefig(table_path, bbox_inches='tight')
        plt.close(fig)
        table_paths.append(table_path)
    return table_paths

SECTION_HEADERS = {
    "Abstract": r"^(Abstract)$",
    "Introduction": r"^(1\s+Introduction)$",
    "Background": r"^(2\s+Background)$",
    "Model Architecture": r"^(3\s+Model Architecture)$",
    "Why Self-Attention": r"^(4\s+Why Self-Attention)$",
    "Training": r"^(5\s+Training)$",
    "Results": r"^(6\s+Results)$",
    "Conclusion": r"^(7\s+Conclusion)$",
    "References": r"^(References)$"
}

def split_sections(full_text):
    lines = full_text.splitlines()
    sections = {name: {"text": [], "images": [], "tables": []} for name in SECTION_HEADERS}
    current = None
    for line in lines:
        for sec, pattern in SECTION_HEADERS.items():
            if re.match(pattern, line.strip(), re.IGNORECASE):
                current = sec
        if current:
            sections[current]["text"].append(line)
    for sec in sections:
        sections[sec]["text"] = "\n".join(sections[sec]["text"]).strip()
    return sections

def build_json(pdf_path, output_json):
    pages = extract_pages(pdf_path)
    table_paths = extract_tables_and_save(pdf_path)
    full_text = "\n".join(p["text"] for p in pages)
    sections = split_sections(full_text)

    # naive mapping: page index to section
    mapping = {
        "Abstract": [0], "Introduction": [1], "Background": [2],
        "Model Architecture": [3], "Why Self-Attention": [4],
        "Training": [5], "Results": [6], "Conclusion": [7], "References": [8]
    }

    # attach images and tables to sections
    for sec, page_idxs in mapping.items():
        for idx in page_idxs:
            if idx < len(pages):
                sections[sec]["images"].extend(pages[idx]["images"])
        if sec == "Results":
            sections[sec]["tables"] = table_paths

    # extract title and authors from page 1 header
    title, authors = "", []
    header = pages[0]["text"].split("Abstract")[0].splitlines()
    if header:
        title = header[0].strip()
        lines = [l.strip() for l in header[1:] if l.strip()]
        email_re = re.compile(r"\S+@\S+")
        for i, line in enumerate(lines):
            if email_re.search(line):
                authors.append({
                    "name": lines[i-2] if i>=2 else "",
                    "affiliation": lines[i-1] if i>=1 else "",
                    "email": line
                })

    output = {"Title": title, "Authors": authors}
    output.update(sections)

    with open(output_json, "w") as f:
        json.dump(output, f, indent=2)

# Run
build_json("/Users/michellenguyen/Documents/ECHALLENGE_SYNAPSIS/NIPS-2017-attention-is-all-you-need-Paper.pdf", "paper_structured.json")
