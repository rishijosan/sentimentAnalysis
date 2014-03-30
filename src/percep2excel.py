'''
Created on 09-Mar-2014

@author: Abhinav
'''
import xlwt
import os


from Perceptron import output,filenm






#create workbook with worksheets
workbook = xlwt.Workbook()
sheet4 = workbook.add_sheet('sheet4',cell_overwrite_ok=True)

sheet4.write(0,0,'Filename(Positive files followed by Negative files)')
sheet4.write(0,1,'Actual Output')
sheet4.write(0,2,'Perceptron Output')


#Actual sentiment of files
act_output = list()


inneg = 'C:/Users/Abhinav/Desktop/Course work/NLP/txt_sentoken/neg_test'
for filename in os.listdir(inneg):
    act_output.append('NEGATIVE')


inpost = 'C:/Users/Abhinav/Desktop/Course work/NLP/txt_sentoken/pos_test'
for filename in os.listdir(inpost):
    act_output.append('POSITIVE')

   

#write to worksheet, column 0 filename, column 1 actual output, column 2 predicted output
column_number = 0
for row_number, item in enumerate(filenm):
    sheet4.write(row_number, column_number, item)

column_number = 1
for row_number, item in enumerate(act_output):
    sheet4.write(row_number, column_number, item)

column_number = 2
for row_number, item in enumerate(output):
    sheet4.write(row_number, column_number, item)


#save to excel
workbook.save('test.xls')
