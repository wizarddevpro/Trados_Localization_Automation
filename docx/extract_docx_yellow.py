from docx import Document
from docx.enum.text import WD_COLOR_INDEX
import nltk


def extract_yellow_sentences(docx_path):
    doc = Document(docx_path)
    highlighted_chunks = []

    def para_has_yellow(para):
        return any(
            run.font.highlight_color == WD_COLOR_INDEX.YELLOW for run in para.runs
        )

    all_paragraphs = []

    # main body
    all_paragraphs.extend(doc.paragraphs)

    # tables
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                all_paragraphs.extend(cell.paragraphs)

    # shapes / textboxes
    for part in doc._part.package.parts:
        if (
            part.content_type
            == "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"
        ):
            continue
        try:
            subdoc = Document(part.blob)
            all_paragraphs.extend(subdoc.paragraphs)
        except:
            pass

    for para in all_paragraphs:
        if para_has_yellow(para):
            text = para.text.strip()
            if text:
                # segment sentences
                sents = nltk.sent_tokenize(text)
                highlighted_chunks.extend(sents)

    return highlighted_chunks
