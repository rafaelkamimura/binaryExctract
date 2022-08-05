import pandas as pd
from pathlib import Path

try:
    f = open('input/L2207018.000','rb')
    
    while True:
        binarycontent = f.read(-1)
        
        if not binarycontent:
            break
        output1 = open("output/dat/L2207018.dat", "w")
        output2 = open("output/txt/L2207018.txt", "w")
        output3 = open("output/csv/L2207018.csv", "w")
        output4 = open("output/xlsx/L2207018.xlsx", "w")
        n1 = output1.write(str(str(binarycontent).split('\\x')))
        n2 = output2.write(str(str(binarycontent).split('\\x')))
        print('Formatação concluída')
        df = pd.DataFrame((str(binarycontent).split('\\x')))
        df.to_csv("output/csv/L2207018.csv")
        print('Arquivo .csv gerado')
        df.to_excel("output/xlsx/L2207018.xlsx")
        print('Planilha gerada')


except IOError:
    print('Error While Opening the file!')

