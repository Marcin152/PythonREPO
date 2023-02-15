import datetime
from datetime import date
import os

#fileIsOk = False
#t = 0
#while not fileIsOk:

    # filename = input('Enter path to results file: ')
    #
    # if os.path.isfile(filename):
    #     fileIsOk = True
    #     print("The results file is %s " % (filename))
    # elif (t<3):
    #     t += 1
    #     print("File name is not correct")
    # elif (t>=3):
    #     print("Go away")
    #     break

#LAB

data_output = 'c:\\temp\data_input'
data_output_catalog = 'c\\temp\data_output'
today = date.today()
is_input_catalog_ok = os.path.isdirectory(data_output_catalog)
is_output_catalog_ok = os.path.isdirectory
data_output_catalog = today.strftime("%Y-%m-%d")
if os.path.isdirectory(filename):
    x = True
else:
    x = False



