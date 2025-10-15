#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime, sys

def create_pdf(outpath, author="Donald Paul Smith (FatherTime)"):
    c = canvas.Canvas(outpath, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, height-72, "Non-Integration and Authorship Declaration")
    c.setFont("Helvetica", 11)
    y = height-110
    lines = [
        f"Author: {author}",
        f"Date (UTC): {datetime.datetime.utcnow().isoformat()}Z",
        "",
        "Declaration of Ownership and Non-Integration:",
        "I hereby declare that all SDKP, SD&N, EOS, QCC0, LLAL, and related frameworks",
        "authored by me remain my intellectual property and have not been integrated",
        "into OpenAI's internal models, training corpora, or derivative systems without",
        "my explicit, written permission.",
        "",
        "Document prepared for archival and legal provenance.",
        "",
        "Signature:",
        "",
        "__________________________",
        author
    ]
    for line in lines:
        c.drawString(72, y, line)
        y -= 14
    c.showPage()
    c.save()

if __name__ == "__main__":
    out = "NonIntegration_Declaration.pdf"
    if len(sys.argv) > 1:
        out = sys.argv[1]
    create_pdf(out)
    print("Saved:", out)
