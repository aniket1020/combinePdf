#!/usr/bin/env python3
import os,sys,re
from PIL import Image
from io import BytesIO
from pdfrw import PdfReader, PdfWriter

def mergeFiles(inputFilesPaths,outputFilePath):
    outputFile = PdfWriter()
    for path in inputFilesPaths:
        try:
            if re.search('.jpg|.png|.jpeg$',path):
                file = BytesIO()
                img=Image.open(path).convert('RGB')
                img.save(file,format="PDF",resolution=100.0)
                file.seek(0)
                outputFile.addpages(PdfReader(file).pages)
            else:
                pdfFile = PdfReader(path)
                outputFile.addpages(pdfFile.pages)
        except:
            print(f"Error: {path}")
            exit()
    with open(outputFilePath,'wb') as out:
        outputFile.write(out)

if __name__ ==  '__main__':
    inputFilesPaths = sys.argv[1:-1]
    outputFilePath = sys.argv[-1]
    if outputFilePath.endswith('.pdf'):
        mergeFiles(inputFilesPaths, outputFilePath)
    else:
        print("Error: Output File path absent")
        exit()
