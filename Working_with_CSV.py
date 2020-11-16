#REFERENCE LINK-----https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/15-PDFs-and-Spreadsheets/00-Working-with-CSV-Files.ipynb

#TO READ DATA IN A CSV FILE
import csv
data= open('example.csv',encoding='utf-8')
csv_data=csv.reader(data)
data_lines=list(csv_data)
for lines in data_lines[1:]:
    print(lines[1]+' '+lines[2])

#TO WRITE A NEW FILE AND ADD DATA INTO IT
file=open('to_open.csv',mode='w',newline='')
file_writer=csv.writer(file,delimiter=',')
file_writer.writerow(['a','b','c'])
file_writer.writerows([['d','e','f'],['1','2','3']])
file.close()

#TO WRITE DATA INTO AN EXISTING FILE
file=open('to_open.csv',mode='a',newline='')
csv_write=csv.writer(file)
csv_write.writerow(['new','new','new'])
file.close()