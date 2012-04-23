#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import csv

#caching groups
product_group_data_read = csv.reader(open('haushalt-gruppen.csv', 'rb'), delimiter=',', quotechar='"');

product_group_data = []
for product_group_data_row in product_group_data_read:
  product_group_data.append([product_group_data_row[0], product_group_data_row[1]])
product_group_data_read = 0

product_data = csv.reader(open('haushalt-bochum-10-2011.csv', 'rb'), delimiter=',', quotechar='"')

#first line
print "uniqueid,produktbereich.id,produktbereich.label,produkt.id,produkt.label,type,year,amount,earning,expense"

# some definitions
current_line = -1
current_product_id = -1
current_product_name = ""
current_product_group_id = -1
current_product_group_name = ""
year = 0
unique_id = 1

for product_data_row in product_data:
  if (current_line == -1):
    current_line+=1
  elif (current_line == 0):
    current_line+=1
    current_product_id = product_data_row[0]
    current_product_name = product_data_row[1]
    current_product_group_id = current_product_id[:2]
    current_product_group_name = "undefined"
    for product_group_data_row in product_group_data:
      if (current_product_group_id == product_group_data_row[0]):
        current_product_group_name = product_group_data_row[1]
    current_product_id = int(current_product_id)
    current_product_group_id = int(current_product_group_id)
  elif (current_line > 0):
    current_year = 2008 + current_line
    current_value = product_data_row[26].replace(".", "")
    if (current_value == ""):
      current_value = 0
    current_value = int(current_value)
    if (current_value < 0):
      current_earning = -1 * current_value
      current_expense = 0
      current_type = "earning"
    else:
      current_earning = 0
      current_expense = current_value
      current_type = "expense"
    print "%s,%s,\"%s\",%s,\"%s\",\"%s\",%s,%s,%s,%s"%(unique_id, current_product_group_id, current_product_group_name, current_product_id, current_product_name, current_type, current_year, current_value, current_earning, current_expense)
    unique_id+=1
    if (current_line == 7):
      current_line = 0
    else:
      current_line+=1

      
