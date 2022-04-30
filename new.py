#run the below commands in your current environment
#! pip install -r requirements.txt
#conda install -c conda-forge poppler

import os
from pdf2image import convert_from_path
from PyPDF3 import PdfFileReader
import pytesseract
from PIL import Image

for i in os.listdir():
    if not i.startswith('.'):
        if ".pdf" in i:
            print(" we are going to consider this pdf file {}".format(i))
            pdf=i
            break
path="C:/Users/ganes/Desktop/aws/"

try:
    pdfname=path+pdf
except(NameError):
    print("File Not Found!!")
    exit()
    
inputpdf = PdfFileReader(open(pdfname,"rb"))
maxPages = inputpdf.numPages
i = 1
check=[]
for page in range(0, maxPages, 10):
    pil_images = convert_from_path(pdfname, dpi=200, first_page=page,
                                                     last_page=min(page + 10 - 1, maxPages), fmt= 'jpg',
                                                     thread_count=1, userpw=None,
                                                     use_cropbox=False, strict=False)
    for image in pil_images:
        check.append(str(i)+".jpg")
        image.save(path+str(i)+ '.jpg', 'JPEG')
        i = i + 1
print("Total Pages:{}".format(maxPages))
text=""
for i in range(len(check)):
    print("Completed page {}".format(i+1))
    text+=pytesseract.image_to_string(Image.open(check[i]))
    os.remove(check[i])
with open(path+"\\output.txt",'w') as f: f.write(str(text))

output=os.path.exists("output.txt")
if output==True:
    for i in os.listdir():
        if "output.txt" in i:
            print("New file created with 'Output.txt' name in the current directory")
else:
    print("Error! Problem with Code or PDF File")