import fitz
import nltk


def extract_pdf_full(pdf_path):
    doc = fitz.open(pdf_path)
    segments = []
    mapping = []

    for page_no in range(len(doc)):
        page = doc[page_no]
        text = page.get_text("text")

        for sent in nltk.sent_tokenize(text):
            sent = sent.strip()
            if not sent:
                continue
            seg_id = f"p{page_no+1}_s{len(segments)+1}"
            segments.append((seg_id, sent))
            mapping.append(
                {
                    "seg_id": seg_id,
                    "page": page_no + 1,
                    "section": None,
                    "text_preview": sent[:60],
                }
            )

    return segments, mapping
