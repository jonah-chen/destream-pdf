import pikepdf # pip3 install pikepdf
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="the path to the pdf file to download all the videos from")
args = parser.parse_args()

file = args.file
pdf_file = pikepdf.Pdf.open(file)

with open("downloaded.txt", "r") as f:
    downloaded = set(f.readlines())

urls = set()

# iterate over PDF pages
for page in pdf_file.pages:
    for annots in page.get("/Annots"):
        uri = annots.get("/A").get("/URI")
        if uri is not None and not uri in downloaded:
            urls.add(str(uri) + "\n")
with open("queue.txt", "w") as f:
    f.writelines(urls, )

print("Total URLs extracted:", len(urls))

