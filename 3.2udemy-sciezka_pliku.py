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

data_input_catalog = 'c:\\temp\data_input'
data_output_catalog = 'c\\temp\data_output'

today = date.today()
data_output_catalog = today.strftime("%Y-%m-%d")
today_output_catalog = data_output_catalog + today.strftime("%Y-%m-%d")

is_input_catalog_ok = os.path.isfile(data_input_catalog)
is_output_catalog_ok = os.path.isfile(data_output_catalog)
is_today_output_catalog_ok = not(os.path.isdir(today_output_catalog)) and not(os.path.isdir(today_output_catalog))

if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print("All conditions fine")
else:
    print("Conditions not met")

if not is_input_catalog_ok:
    print("Input catalog %s must exists!" % data_input_catalog)
if not is_output_catalog_ok:
    print("Output catalog %s must exists!" % data_output_catalog)
if not is_today_output_catalog_ok:
    print("Today's output %s cannot exists (neither as file nor as directory!" %today_output_catalog)

