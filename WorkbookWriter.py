
from pathlib import Path
from openpyxl import load_workbook, Workbook 
from datetime import date

# PATH='Attend.xlsx'
# wb = load_workbook(filename=PATH, read_only=False)
# rng=wb["Sheet1"]["A1":"D6"]
# rng[0][0].offset(row=0, column=0).value = 'Marks Mom'
# for cells in rng:
#     for cell in cells:
#         print(cell.value,end = " ")
#     print()
# cell.offset(row=0, column=0).value = ''


class WorkbookWriter:
    def __init__(self,path):
        self.path = path
        self.workbook = load_workbook(filename=path, read_only=False)
    
        self.date = str(date.today())

    def write(self,rollno,present,display = False):

        day = int(self.date.split("-")[-1])

        rng = self.workbook[self.getCurrentSheet()]["A1":"AL160"]

        rln = int(rollno[-2:])


        rng[rln+1][day+1].value="P" if present else "A"

        if(display):
            for cells in rng:
                for cell in cells:
                    print(cell.value,end = " ")
                print()

        self.workbook.save(self.path)

    def getCurrentSheet(self):
        # "year-month"
        return self.date[:7]


        




    
    
# a = WorkbookWriter("Attend.xlsx")
# a.write("003",True)
# a.show()
# a.savewb()

