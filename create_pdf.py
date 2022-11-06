from PyPDF2 import PdfReader, PdfWriter

def func(path, aog, n):
    reader = PdfReader(path)
    writer = PdfWriter()

    for i in range(reader.getNumPages()):
        if i+1 == n:
            writer.add_page(reader.pages[i])
            writer.pages[i].rotate(aog)
        else:
            writer.add_page(reader.pages[i])
    with open("output.pdf", "wb") as output:
        writer.write(output)

    return f'The page doesnt exist in the pdf'

print("Enter complete file path: ")
path = input(r'')
aog = int(input("Enter the angle of rotation: "))
n = int(input("Enter the page number: "))
output = func(path, aog, n)