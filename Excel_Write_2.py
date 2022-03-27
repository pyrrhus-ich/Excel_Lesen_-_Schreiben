from re import A
from openpyxl import Workbook, workbook as wb

wb=Workbook()
ws=wb.active
myList=['Frank','hat','bald','Geburtstag']

for el in myList:
    i=1
    cell="A"
    ws[cell+str(i)]=myList[i-1]
    i+=1
wb.save('Bsp_Excel_Write_2.xlsx')

