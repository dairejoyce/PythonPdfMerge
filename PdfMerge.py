import fitz  # pip3 install PyMuPDF


def merge(pdfs):
    result = fitz.open()

    for pdf in pdfs:
        with fitz.open(pdf) as file:
            result.insert_pdf(file)

    result.save('./pdfs/merged.pdf', deflate=True)

    return None
