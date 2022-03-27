from openpyxl import Workbook
from openpyxl.utils import get_column_letter

wb = Workbook()
ws = wb.active
myList=['Frank','hatte','gestern','Geburtstag']

for x in list(range(1,len(myList)+1)):
    ch = get_column_letter(x)
    print(ch)



