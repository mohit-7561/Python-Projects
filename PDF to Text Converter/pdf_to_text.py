import PyPDF2
info = PyPDF2.PdfReader("sample-pdf-file.pdf")

str = ""
for i in range(0, len(info.pages)):
    str += info.pages[i].extract_text()

with open("sample.txt", "w", encoding="utf-8") as f:
    f.write(str)