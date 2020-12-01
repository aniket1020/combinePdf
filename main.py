import os,sys,re
from PIL import Image
from pdfrw import PdfReader, PdfWriter

def mergeFiles(inputFilesPaths,outputFilePath):
    outputFile = PdfWriter()
    for path in inputFilesPaths:
        try:
            if re.search('.jpg|.png|.jpeg$',path):
                img=Image.open(path).convert('RGB')
                img.save('#_tmp_#.pdf',"PDF",resolution=100.0)
                outputFile.addpages(PdfReader('#_tmp_#.pdf').pages)
            else:
                pdfFile = PdfReader(path)
                outputFile.addpages(pdfFile.pages)
        except:
            print(f"Error: {path}")
            return
    with open(outputFilePath,'wb') as out:
        outputFile.write(out)

if __name__ ==  '__main__':
    inputFilesPaths = sys.argv[1:-1]
    outputFilePath = sys.argv[-1]
    mergeFiles(inputFilesPaths, outputFilePath)
    try:
        os.remove('./#_tmp_#.pdf')
    except:
        pass
