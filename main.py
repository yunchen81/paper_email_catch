from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf

from os import listdir
from os.path import isfile, join

import csv

def read_pdf(pdf):
    try:
        # resource manager
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        laparams = LAParams()
        # device
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        process_pdf(rsrcmgr, device, pdf)
        device.close()
        content = retstr.getvalue()
        retstr.close()
        # 獲取所有行
        context = str(content).split("\n")
      
    #    print(context)
    
        for lines in context:
            if '@' in lines:
                return lines
                detail = lines.split(' ')
                for s in detail:
                    if '@' in s:
                        #print(s)
                        return s
    except:
        print('file error')
        
def _main():
    

    mypath = 'downloadedPDF'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    email_array = []
    file_count=1
    for file in onlyfiles:
        print(' processing',file,'...',file_count,'/',len(onlyfiles))
        filepath = mypath + '/' + file
# =============================================================================
#         print(filepath)
# =============================================================================
        my_pdf = open(filepath, "rb")
        email_array.append([file,read_pdf(my_pdf)])
# =============================================================================
#         print(email_array)
# =============================================================================
        my_pdf.close()
        file_count+=1

    with open('email.csv', 'w', newline='') as csvfile:
        writer  = csv.writer(csvfile)
# =============================================================================
#         writer.writerow(email_array)    
# =============================================================================
        for row in email_array:
            try:
                writer.writerow(row)  
            except:
                pass
        

if __name__ == '__main__':
    _main()