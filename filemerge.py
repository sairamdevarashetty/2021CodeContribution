from PyPDF2 import PdfFileMerger
from os import listdir
from os.path import isfile, join
import sys 

def pdf_cat(parameters):
    base_dir = parameters
    directories = sorted(listdir(base_dir))
    for dir in directories:
        pdfs = sorted(listdir(base_dir+"/"+dir))

        pdfs.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
        
        merger = PdfFileMerger()

        for pdf in pdfs:
            merger.append(base_dir+ "/"+dir+"/" + pdf)

        merger.write(dir+".pdf")
        merger.close()


if __name__ == '__main__':
    pdf_cat(sys.argv[1:])

    
