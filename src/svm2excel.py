'''
Created on Mar 12, 2014

@author: root
'''
import xlwt
import os
#from HW1 import *

from SVM import opt

#print output





workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)

sheet1.write(0,0,'Filename(Positive files followed by Negative files)')
sheet1.write(0,1,'Actual Output')
sheet1.write(0,2,'SVM Output')

filenm = list()
act_output = list()

inneg = '/media/sf_G_DRIVE/nlp/txt_sentoken/negtest'
for filename in os.listdir(inneg):
    filenm.append(filename)
    act_output.append('0')


inpost = '/media/sf_G_DRIVE/nlp/txt_sentoken/postest'
for filename in os.listdir(inpost):
    filenm.append(filename)
    act_output.append('1')

#files = list()

#unigram_output =  posUniGr + negUniGr
#bigram_output =  posBiGr + negBiGr



   
#sheet.write(rowIdx,0,files) 

column_number = 0
for row_number, item in enumerate(filenm):
    sheet1.write(row_number, column_number, item)

column_number = 1
for row_number, item in enumerate(act_output):
    sheet1.write(row_number, column_number, item)

column_number = 2
for row_number, item in enumerate(opt):
    sheet1.write(row_number, column_number, item)




workbook.save('test1.xls')
